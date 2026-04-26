from selenium.webdriver.common.by import By


class AutoCompletePageLocators: 
    MULTIPLE_INPUT = (By.CSS_SELECTOR, "#autoCompleteMultipleInput")
    SINGLE_INPUT = (By.CSS_SELECTOR, "#autoCompleteSingleInput")
    MULTIPLE_RESULT = (By.CSS_SELECTOR, ".auto-complete__multi-value")
    SINGLE_RESULT = (By.CSS_SELECTOR, ".auto-complete__single-value ")
    AUTO_COMPLETE_OPTIONS = (By.CSS_SELECTOR, ".auto-complete__option")