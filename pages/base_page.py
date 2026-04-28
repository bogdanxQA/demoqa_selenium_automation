from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select



class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url




    def open(self):
        self.driver.get(self.url)
        
    def wait_element_stable(self, element, timeout=5):
        WebDriverWait(self.driver, timeout).until(
        lambda d: element.is_displayed() and element.size['width'] > 0 and element.size['height'] > 0
        )

    def element_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def element_is_not_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))   

    def elements_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))    
    
    #взять текст из инпута
    def element_is_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))   
         
    def elements_are_presents(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))  

    def element_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def value_in_element_is_present(self, locator, value, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, value))
    
    def text_in_element_is_present(self, locator, value, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, value))
    
    def wait_for_element_text_in_list(self, locator, text:str, timeout = 5):
        elements = self.elements_are_presents(locator, timeout)
        expected = text
        for element in elements:
            if element.text == expected:
                return element
        raise TimeoutException(f"Элемент с текстом '{expected}' не найден среди заданных локаторов")
    
    """Ожидает, пока элементы будут иметь непустой текст."""
    def wait_for_elements_to_have_text(self, locator, timeout=10):
   
        elements = self.elements_are_presents(locator, timeout)  # ждём, что хотя бы один элемент появился
        WebDriverWait(self.driver, timeout).until(
            lambda d: all(el.text.strip() != '' for el in elements)
        )
        return elements
    
    # def text_contains_in_element(self, locator, substring, timeout=10):
    #     print(f"Ожидание текста '{substring}' в элементе {locator}, таймаут {timeout} сек")
    #     return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, substring))

    def wait_for_alert(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
    
    def is_alert_closed(self, timeout=1):

        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return False
        except TimeoutException:
            return True
        
    """Ждёт, пока элемент, заданный локатором, станет невидимым или исчезнет из DOM"""
    def wait_for_element_to_disappear(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    def select_by_text(self, locator, text:str, timeout:int = 10):
        element = self.element_is_present(locator, timeout)
        select = Select(element)
        select.select_by_visible_text(text)
        return select.first_selected_option.text

    def drag_and_drop_by_offset(self, element, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x, y)
        action.perform()

    def drag_and_drop_elements(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where).pause(0.05)
        action.perform()

    def manual_drag_and_drop_elements(self, source, target):
        action = ActionChains(self.driver)
        action.click_and_hold(source).pause(0.2).move_to_element(target).pause(0.2).release(target).perform()

    def drag_and_drop_with_offset(self, source, target, y_offset=10):
        action = ActionChains(self.driver)
        action.click_and_hold(source).pause(0.1)
        action.move_to_element(target).move_by_offset(0, y_offset).pause(0.1)
        action.release().perform()
        

    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).move_to_element(element)
        action.perform()

    def right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
    

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def tab_or_window_is_opened(self, count, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(count))

        

