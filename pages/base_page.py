from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException



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
        

    
    
    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).move_to_element(element)
        action.perform()

    def right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()
    

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def tab_or_window_is_opened(self, count, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(count))

        

