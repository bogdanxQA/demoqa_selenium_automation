from pages.base_page import BasePage
from locators.accordian_page_locators import AccodrianPageLocators
from locators.auto_complete_page_locators import AutoCompletePageLocators
from locators.date_picker_page_locators import DatePickerPageLocators
from locators.slider_page_locators import SliderPageLocators
from locators.progress_bar_page_locators import ProgressBarPageLocators
from locators.tool_tips_page_locators import ToolTipsPageLocators
from locators.tabs_page_locators import TabsPageLocators
from locators.menu_page_locators import MenuPageLocators
from locators.select_menu_page_locators import SelectMenuPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data.data import COLORS, OPTIONS_FOR_ONE, OPTIONS_FOR_VALUE
from selenium.webdriver.common.keys import Keys
import random
from data.generator.generator import date_generated
from datetime import datetime
import time
import allure


class AccordianPage(BasePage):

    locators = AccodrianPageLocators()

    """Здесь падает 3 тест, так как текст не успевает загрузиться, возможно из-за анимаций js. Ума обойти это не хватило пока что"""
    def open_get_and_close_content_from_accordian_MINE(self, number):
        element = self.elements_are_visible(self.locators.ACCORDIAN_BUTTON)[number]
        if element.get_attribute("aria-expanded") == "false":
            element.click()
        
        title = element.text
        # time.sleep(1)
        content_element = self.elements_are_presents(self.locators.ACCORDIAN_CONTENT)[number]
        WebDriverWait(self.driver, 3).until(lambda d: len(content_element.text.strip()) > 0)
        content = content_element.text
        element.click()
        is_opened = element.get_attribute("aria-expanded")
        
        return title, content, is_opened
    

    """Вариант от нейронки исправленный. Стабильный"""
    @allure.step("Open, read and close accordion section {number}")
    def open_get_and_close_content_from_accordian(self, number):
        buttons = self.elements_are_visible(self.locators.ACCORDIAN_BUTTON)
        button = buttons[number]
        if button.get_attribute("aria-expanded") == "false":
            button.click()

        title = button.text

        # Находим родительский .accordion-item для этой кнопки
        accordion_item = button.find_element(By.XPATH, "./ancestor::div[contains(@class, 'accordion-item')]")
        # Внутри него ищем видимый блок контента (accordion-body)
        with allure.step("Wait for content to become visible"):
            content_element = WebDriverWait(accordion_item, 10).until(
                EC.visibility_of_element_located((By.XPATH, ".//div[contains(@class, 'accordion-body')]"))
            )
            # Дополнительно ждём непустой текст (для надёжности)
            WebDriverWait(self.driver, 5).until(lambda d: len(content_element.text.strip()) > 0)
        content = content_element.text

        # Закрываем (опционально)
        button.click()
        is_opened = button.get_attribute("aria-expanded")
        return title, content, is_opened
    

class AutoCompletePage(BasePage):

    locators = AutoCompletePageLocators()
    
    @allure.step("Fill multiple input with random colors")
    def random_fill_multiple_input(self):

        k = random.randint(1, len(COLORS))

        chosen_lables = random.sample(COLORS, k)
        self.element_is_visible(self.locators.MULTIPLE_INPUT).clear()
        for i in chosen_lables:
            with allure.step(f"Add color '{i}'"):
                element = self.element_is_visible(self.locators.MULTIPLE_INPUT)
                element.send_keys(i)
                self.value_in_element_is_present(self.locators.MULTIPLE_INPUT, value=i)
                self.element_is_present(self.locators.AUTO_COMPLETE_OPTIONS)
                element.send_keys(Keys.ENTER)
                self.value_in_element_is_present(self.locators.MULTIPLE_INPUT, value="")
        return chosen_lables

    @allure.step("Get displayed colors from multiple input")
    def get_data_from_multiple_input(self):
        color_elements = self.elements_are_presents(self.locators.MULTIPLE_RESULT)
        displayed_value = []
        for color in color_elements:
            displayed_value.append(color.text)
        return displayed_value

    @allure.step("Fill single input with random color")
    def random_fill_single_input(self):
        chosen_color = random.choice(COLORS)
        with allure.step(f"Select color '{chosen_color}'"):
            element = self.element_is_visible(self.locators.SINGLE_INPUT)
            element.clear()
            element.send_keys(chosen_color)
            self.value_in_element_is_present(self.locators.SINGLE_INPUT, value=chosen_color)
            self.element_is_present(self.locators.AUTO_COMPLETE_OPTIONS)
            element.send_keys(Keys.ENTER)
        return chosen_color

    @allure.step("Get displayed color from single input")
    def get_data_from_single_input(self):
        displayed_value = self.element_is_present(self.locators.SINGLE_RESULT).text
        return displayed_value

class DatePickerPage(BasePage):

    locators = DatePickerPageLocators()

    @allure.step("Select random date")
    def select_date(self):
        date = next(date_generated())
        input_date = self.element_is_visible(self.locators.SELECT_DATE_INPUT)
        input_date.click()
        with allure.step(f"Set month: {date.month}, year: {date.year}"):
            self.select_by_text(self.locators.SELECT_MONTH, date.month)
            self.select_by_text(self.locators.SELECT_YEAR, date.year)
        with allure.step(f"Click on day {date.day}"):
            element = self.wait_for_element_text_in_list(self.locators.SELECT_DAY, date.day)
            # real_date = element.get_attribute("aria-label")
            element.click()
        date_after = input_date.get_attribute("value")
        month_num = datetime.strptime(date.month, "%B").month
        return date_after, date.day, month_num, date.year
    
    @allure.step("Select random date and time")
    def select_data_and_time(self):
        date = next(date_generated())
        input_date = self.element_is_visible(self.locators.SELECT_DATE_TIME_INPUT)
        input_date.click()
        with allure.step("Open month dropdown and select month"):
            self.element_is_visible(self.locators.SELECT_MONTH_DATE_TIME).click()
            self.wait_for_element_text_in_list(self.locators.MONTH_DROPDOWN, date.month).click()
        with allure.step("Open year dropdown and select year"):
            self.element_is_visible(self.locators.SELECT_YEAR_DATE_TIME).click()
            self.wait_for_element_text_in_list(self.locators.YEAR_DROPDOWN, date.year_short).click()
        with allure.step(f"Select day {date.day}"):
            self.wait_for_element_text_in_list(self.locators.SELECT_DAY, date.day).click()
        with allure.step(f"Select time {date.time}"):
            self.wait_for_element_text_in_list(self.locators.SELECT_TIME, date.time).click()
        displayed_date_and_time = input_date.get_attribute("value")
        our_dt = datetime.strptime(f"{date.month} {date.day}, {date.year_short} {date.time}", "%B %d, %Y %H:%M")
        displayed_dt = datetime.strptime(displayed_date_and_time, "%B %d, %Y %I:%M %p")
        return our_dt, displayed_dt
    
class SliderPage(BasePage):

    locators = SliderPageLocators()

    @allure.step("Move slider to random position")
    def move_slider(self):
        slider = self.element_is_visible(self.locators.SLIDER)
        self.scroll_to_element(slider)
        value_before = slider.get_attribute("value")
        with allure.step(f"Drag slider by {offset}px horizontally"):
            time.sleep(0.1)
            self.drag_and_drop_by_offset(slider, random.randint(26, 100), 0)
        value_after = slider.get_attribute("value")
        return value_before, value_after
    

class ProgressBarPage(BasePage):

    locators = ProgressBarPageLocators()

    @allure.step("Start/stop progress bar and get values before and after")
    def start_stop_progress_bar(self):
        before = self.element_is_present(self.locators.PROGRESS_BAR).text
        start_stop = self.element_is_visible(self.locators.START_STOP_BUTTON)
        with allure.step("Start progress bar"):
            start_stop.click()
        time.sleep(random.uniform(1, 6))  
        with allure.step("Stop progress bar"):
            start_stop.click()
        after = self.element_is_present(self.locators.PROGRESS_BAR).text
        return after, before
    
    @allure.step("Wait for 100% . and reset progress bar")
    def reset_full_progress_bar(self):
        before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute("style").split("width:")[1].strip().split(";")[0]
        start_stop = self.element_is_visible(self.locators.START_STOP_BUTTON)
        with allure.step("Start progress bar and wait until 100%"):
            start_stop.click()
            self.text_in_element_is_present(self.locators.PROGRESS_BAR, "100%", timeout=10)
        with allure.step("Click reset button"):
            reset = self.element_is_visible(self.locators.RESET_BUTTON, timeout=12)
            reset.click()
        with allure.step("Verify progress bar resets to 0%"):
            self.text_in_element_is_present(self.locators.PROGRESS_BAR, "0%", timeout=10)
            time.sleep(0.5)
            after = self.element_is_present(self.locators.PROGRESS_BAR).text
        return after, before
    
class TabsPage(BasePage):

    locators = TabsPageLocators()

    @allure.step("Open 'What' tab and get its content")
    def open_what_tab_and_get_content(self):

        what_tab = self.element_is_visible(self.locators.WHAT_TAB)
        if what_tab.get_attribute("aria-selected") == 'true':
            content = self.element_is_visible(self.locators.WHAT_TAB_CONTENT).text
        else:
            with allure.step("Click on 'What' tab"): 
                what_tab.click()
            content = self.element_is_visible(self.locators.WHAT_TAB_CONTENT).text
        is_opened = what_tab.get_attribute("aria-selected")
        return content, is_opened
    
    @allure.step("Open 'Origin' tab and get its content")
    def open_origin_tab_and_get_content(self):

        origin_tab = self.element_is_visible(self.locators.ORIGIN_TAB)
        if origin_tab.get_attribute("aria-selected") == 'true':
            content = self.element_is_visible(self.locators.ORIGIN_TAB_CONTENT).text
        else:
            with allure.step("Click on 'Origin' tab"): 
                origin_tab.click()
            content = self.element_is_visible(self.locators.ORIGIN_TAB_CONTENT).text
        is_opened = origin_tab.get_attribute("aria-selected")
        return content, is_opened
    
    @allure.step("Open 'Use' tab and get its content")
    def open_use_tab_and_get_content(self):

        use_tab = self.element_is_visible(self.locators.USE_TAB)
        if use_tab.get_attribute("aria-selected") == 'true':
            content = self.element_is_visible(self.locators.USE_TAB_CONTENT).text
        else:
            with allure.step("Click on 'Use' tab"): 
                use_tab.click()
            content = self.element_is_visible(self.locators.USE_TAB_CONTENT).text
        is_opened = use_tab.get_attribute("aria-selected")
        return content, is_opened
    
    @allure.step("Open 'More' tab and get its content")
    def open_more_tab_and_get_content(self):

        more_tab = self.element_is_visible(self.locators.MORE_TAB)
        if more_tab.get_attribute("aria-selected") == 'true':
            content = self.element_is_visible(self.locators.MORE_TAB_CONTENT).text
        else:
            with allure.step("Click on 'More' tab"): 
                more_tab.click()
            content = self.element_is_visible(self.locators.MORE_TAB_CONTENT).text
        is_opened = more_tab.get_attribute("aria-selected")
        return content, is_opened
    
class ToolTipsPage(BasePage):

    locators = ToolTipsPageLocators()

    @allure.step("Hover over button and get tooltip text")
    def hover_to_button_and_get_content(self):
        button = self.element_is_visible(self.locators.HOVER_ME_BUTTON)
        time.sleep(0.05)
        with allure.step("Move mouse to button"):
            self.move_to_element(button)
        self.element_is_visible(self.locators.AFTER_HOVER_BUTTON)
        content = self.element_is_visible(self.locators.HOVER_CONTENT).text
        return content
    
    @allure.step("Hover over input field and get tooltip text")
    def hover_to_input_and_get_content(self):
        input = self.element_is_visible(self.locators.HOVER_ME_INPUT)
        time.sleep(0.05)
        with allure.step("Move mouse to input field"):
            self.move_to_element(input)
        self.element_is_visible(self.locators.AFTER_HOVER_INPUT)
        content = self.element_is_visible(self.locators.HOVER_CONTENT).text
        return content
    
    @allure.step("Hover over 'Contrary' link and get tooltip text")
    def hover_to_contrary_and_get_content(self):
        contrary = self.element_is_visible(self.locators.HOVER_CONTRARY)
        time.sleep(0.05)
        with allure.step("Move mouse to 'Contrary' link"):
            self.move_to_element(contrary)
        self.element_is_visible(self.locators.AFTER_HOVER_CONTRARY)
        content = self.element_is_visible(self.locators.HOVER_CONTENT).text
        return content
    
    @allure.step("Hover over text link and get tooltip text")
    def hover_to_text_and_get_content(self):
        text = self.element_is_visible(self.locators.HOVER_TEXT)
        time.sleep(0.05)
        with allure.step("Move mouse to text link"):
            self.move_to_element(text)
        self.element_is_visible(self.locators.AFTER_HOVER_TEXT)
        content = self.element_is_visible(self.locators.HOVER_CONTENT).text
        return content
    

class MenuPage(BasePage):

    locators = MenuPageLocators()
    
    @allure.step("Get all menu items titles")
    def check_menu(self):
        menu_links = self.elements_are_presents(self.locators.MENU_LINKS)
        data = []
        for link in menu_links:
            with allure.step(f"Hover over '{link.text}'"):
                self.move_to_element(link)
                # self.element_is_visible(link)
            data.append(link.text)

        return data


class SelectMenuPage(BasePage):

    locators = SelectMenuPageLocators()

    @allure.step("Select random value in first selector (Select Value)")
    def select_random_value_in_first_selector(self):
        input = self.element_is_visible(self.locators.SELECT_VALUE_INPUT)
        with allure.step("Open dropdown"):
            input.click()
        chosen_option = random.choice(OPTIONS_FOR_VALUE)
        with allure.step(f"Choose '{chosen_option}'"):
            option = self.wait_for_element_text_in_list(self.locators.SELECT_OPTIONS, chosen_option)
            option.click()
        displayed_text = self.wait_for_element_text_in_list(self.locators.DISPLAYED_OPTION, chosen_option).text
        return chosen_option, displayed_text
    
    @allure.step("Select random value in second selector (Select One)")
    def select_random_value_in_second_selector(self):
        input = self.element_is_visible(self.locators.SELECT_ONE_INPUT)
        with allure.step("Open dropdown"):
            input.click()
        chosen_option = random.choice(OPTIONS_FOR_ONE)
        with allure.step(f"Choose '{chosen_option}'"):
            option = self.wait_for_element_text_in_list(self.locators.SELECT_OPTIONS, chosen_option)
            option.click()
        displayed_text = self.wait_for_element_text_in_list(self.locators.DISPLAYED_OPTION, chosen_option).text
        return chosen_option, displayed_text
    
    @allure.step("Select random color in old style select menu")
    def select_random_color_in_old_style_select_menu(self):
        chosen_color = random.choice(COLORS)
        with allure.step(f"Select '{chosen_color}' from old style select"):
            selected_value = self.select_by_text(self.locators.OLD_SELECT, chosen_color)
        return chosen_color, selected_value
    
    @allure.step("Select random colors in multi-select dropdown")
    def multi_select_drop_down(self):
        colors = ["Blue", "Black", "Green", "Red"]
        k = random.randint(1, len(colors))
        chosen_colors = random.sample(colors, k)
        input = self.element_is_visible(self.locators.MULTI_SELECT_DROP_DOWN)
        input.click()
        
        for color in chosen_colors:
            with allure.step(f"Select '{color}'"):
                element = self.wait_for_element_text_in_list(self.locators.SELECT_OPTIONS, color)
                element.click()
        return chosen_colors
    
    @allure.step("Get displayed colors in multi-select")
    def get_displayed_colors_in_multi_select(self):
        elements = self.elements_are_presents(self.locators.DISPLAYED_COLORS_MULTI_SELECT)
        return [element.text for element in elements]
            


    
    



    




 

            





        

        
        


    

    
    


    







