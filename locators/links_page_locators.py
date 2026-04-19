from selenium.webdriver.common.by import By


class LinksPageLocators:                                                                 #xpath:
    SIMPLE_LINK = (By.CSS_SELECTOR, "#simpleLink")                                      # //a[@id = 'simpleLink']      
    NOT_FOUND_LINK = (By.CSS_SELECTOR, "#invalid-url")                                  # //a[@id = 'invalid-url']
