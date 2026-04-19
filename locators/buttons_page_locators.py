from selenium.webdriver.common.by import By


class ButtonsPageLocators:                                                              #xpath:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")                          # //button[@id = 'doubleClickBtn']      
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "#rightClickBtn")                            # //button[@id = 'rightClickBtn']
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")                                       

    DOUBLE_CLICK_MSG = (By.CSS_SELECTOR, "#doubleClickMessage")                         # //p[@id = 'doubleClickMessage']  
    RIGHT_CLICK_MSG = (By.CSS_SELECTOR, "#rightClickMessage")                           # //p[@id = 'rightClickMessage']  
    CLICK_ME_MSG = (By.CSS_SELECTOR, "#dynamicClickMessage")                            # //p[@id = 'dynamicClickMessage']





 
