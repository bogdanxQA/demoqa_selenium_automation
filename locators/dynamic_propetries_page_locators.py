from selenium.webdriver.common.by import By


class DynamicPropertiesPageLocators:
                                                                        #xpath:
    WILL_ENABLE_BUTTON = (By.CSS_SELECTOR, "#enableAfter")              # //button[@id='enableAfter']
    VISIBLE_AFTER_BUTTON = (By.CSS_SELECTOR, "#visibleAfter")           # //button[@id='visibleAfter']  
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "#colorChange")             # //button[@id='colorChange']     
    RANDOM_ID_TEXT = (By.CSS_SELECTOR, "h1 + p")                        #//p[text()='This text has random Id']  так же: div > p   |   div p:first-of-type
