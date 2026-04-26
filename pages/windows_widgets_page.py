from pages.base_page import BasePage
from locators.accordian_page_locators import AccodrianPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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





