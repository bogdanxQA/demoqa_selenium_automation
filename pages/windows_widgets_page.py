from pages.base_page import BasePage
from locators.accordian_page_locators import AccodrianPageLocators
from locators.auto_complete_page_locators import AutoCompletePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data.data import COLORS
from selenium.webdriver.common.keys import Keys
import random



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
    
    def random_fill_multiple_input(self):

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

    







