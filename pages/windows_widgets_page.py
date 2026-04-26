from pages.base_page import BasePage
from locators.accordian_page_locators import AccodrianPageLocators
from locators.auto_complete_page_locators import AutoCompletePageLocators
from locators.date_picker_page_locators import DatePickerPageLocators
from locators.slider_page_locators import SliderPageLocators
from locators.progress_bar_page_locators import ProgressBarPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data.data import COLORS
from selenium.webdriver.common.keys import Keys
import random
from data.generator.generator import date_generated
from datetime import datetime
import time



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
    def open_get_and_close_content_from_accordian(self, number):
        buttons = self.elements_are_visible(self.locators.ACCORDIAN_BUTTON)
        button = buttons[number]
        if button.get_attribute("aria-expanded") == "false":
            button.click()

        title = button.text

        # Находим родительский .accordion-item для этой кнопки
        accordion_item = button.find_element(By.XPATH, "./ancestor::div[contains(@class, 'accordion-item')]")
        # Внутри него ищем видимый блок контента (accordion-body)
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
    
    def pyrandom_fill_multiple_input(self):

        k = random.randint(1, len(COLORS))

        chosen_lables = random.sample(COLORS, k)
        self.element_is_visible(self.locators.MULTIPLE_INPUT).clear()
        for i in chosen_lables:
            element = self.element_is_visible(self.locators.MULTIPLE_INPUT)
            element.send_keys(i)
            self.value_in_element_is_present(self.locators.MULTIPLE_INPUT, value=i)
            self.element_is_present(self.locators.AUTO_COMPLETE_OPTIONS)
            element.send_keys(Keys.ENTER)
            self.value_in_element_is_present(self.locators.MULTIPLE_INPUT, value="")

        return chosen_lables

    def get_data_from_multiple_input(self):
        color_elements = self.elements_are_presents(self.locators.MULTIPLE_RESULT)
        displayed_value = []
        for color in color_elements:
            displayed_value.append(color.text)
        return displayed_value

    def random_fill_single_input(self):
        chosen_color = random.choice(COLORS)
        element = self.element_is_visible(self.locators.SINGLE_INPUT)
        element.clear()
        element.send_keys(chosen_color)
        self.value_in_element_is_present(self.locators.SINGLE_INPUT, value=chosen_color)
        self.element_is_present(self.locators.AUTO_COMPLETE_OPTIONS)
        element.send_keys(Keys.ENTER)
        return chosen_color


    def get_data_from_single_input(self):
        displayed_value = self.element_is_present(self.locators.SINGLE_RESULT).text
        return displayed_value

class DatePickerPage(BasePage):

    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(date_generated())
        input_date = self.element_is_visible(self.locators.SELECT_DATE_INPUT)
        input_date.click()
        self.select_by_text(self.locators.SELECT_MONTH, date.month)
        self.select_by_text(self.locators.SELECT_YEAR, date.year)
        element = self.wait_for_element_text_in_list(self.locators.SELECT_DAY, date.day)
        # real_date = element.get_attribute("aria-label")
        element.click()
        date_after = input_date.get_attribute("value")
        month_num = datetime.strptime(date.month, "%B").month
        return date_after, date.day, month_num, date.year
    

    def select_data_and_time(self):
        date = next(date_generated())
        input_date = self.element_is_visible(self.locators.SELECT_DATE_TIME_INPUT)
        input_date.click()
        self.element_is_visible(self.locators.SELECT_MONTH_DATE_TIME).click()
        self.wait_for_element_text_in_list(self.locators.MONTH_DROPDOWN, date.month).click()
        self.element_is_visible(self.locators.SELECT_YEAR_DATE_TIME).click()
        self.wait_for_element_text_in_list(self.locators.YEAR_DROPDOWN, date.year_short).click()
        self.wait_for_element_text_in_list(self.locators.SELECT_DAY, date.day).click()
        self.wait_for_element_text_in_list(self.locators.SELECT_TIME, date.time).click()
        displayed_date_and_time = input_date.get_attribute("value")
        our_dt = datetime.strptime(f"{date.month} {date.day}, {date.year_short} {date.time}", "%B %d, %Y %H:%M")
        displayed_dt = datetime.strptime(displayed_date_and_time, "%B %d, %Y %I:%M %p")
        return our_dt, displayed_dt
    
class SliderPage(BasePage):

    locators = SliderPageLocators()

    def move_slider(self):
        slider = self.element_is_visible(self.locators.SLIDER)
        self.scroll_to_element(slider)
        value_before = slider.get_attribute("value")
        time.sleep(0.1)
        self.drag_and_drop_by_offset(slider, random.randint(26, 100), 0)
        value_after = slider.get_attribute("value")
        return value_before, value_after
    

class ProgressBarPage(BasePage):

    locators = ProgressBarPageLocators

    def start_stop_progress_bar(self):
        before = self.element_is_present(self.locators.PROGRESS_BAR).text
        start_stop = self.element_is_visible(self.locators.START_STOP_BUTTON)
        start_stop.click()
        time.sleep(random.uniform(1, 6))  
        start_stop.click()
        after = self.element_is_present(self.locators.PROGRESS_BAR).text
        return after, before
    
    def reset_full_progress_bar(self):
        before = self.element_is_present(self.locators.PROGRESS_BAR).text
        start_stop = self.element_is_visible(self.locators.START_STOP_BUTTON)
        start_stop.click()
        self.text_in_element_is_present(self.locators.PROGRESS_BAR, "100%", timeout=10)
        reset = self.element_is_visible(self.locators.RESET_BUTTON, timeout=12)
        reset.click()
        self.text_in_element_is_present(self.locators.PROGRESS_BAR, "0%", timeout=10)
        time.sleep(0.5)
        after = self.element_is_present(self.locators.PROGRESS_BAR).text
        return after, before
    




 

            





        

        
        


    

    
    


    







