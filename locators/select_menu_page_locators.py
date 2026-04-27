from selenium.webdriver.common.by import By


class SelectMenuPageLocators:

    SELECT_VALUE_INPUT = (By.CSS_SELECTOR, "#react-select-2-input")
    SELECT_OPTIONS = (By.CSS_SELECTOR, "div[role='option']") 
    DISPLAYED_OPTION = (By.CSS_SELECTOR, "div[class*='singleValue']")
    SELECT_ONE_INPUT = (By.CSS_SELECTOR, "#react-select-3-input")
    OLD_SELECT = (By.CSS_SELECTOR, "#oldSelectMenu")
    MULTI_SELECT_DROP_DOWN = (By.CSS_SELECTOR, "#react-select-4-input")
    DISPLAYED_COLORS_MULTI_SELECT = (By.CSS_SELECTOR, "div[class = 'css-1p3m7a8-multiValue']")
    
    
    

