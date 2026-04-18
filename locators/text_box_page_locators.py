from selenium.webdriver.common.by import By


class TextBoxPageLocators:
                                                                        #xpath:
    FULL_NAME = (By.CSS_SELECTOR, "#userName")                          # //input[@id='userName']
    EMAIL = (By.CSS_SELECTOR, "#userEmail")                             # //input[@id='userEmail']
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")              # //input[@id='currentAddress']
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")          # //input[@id='permanentAddress']


    #created form
    NAME_CREATED = (By.CSS_SELECTOR, "#name")                           # //p[@id='name']
    EMAIL_CREATED = (By.CSS_SELECTOR, "#email")                         # //p[@id='email']
    CURRENT_ADDRESS_CREATED = (By.CSS_SELECTOR, "p#currentAddress")     # //p[@id='currentAddress']
    PERMANENT_ADDRESS_CREATED = (By.CSS_SELECTOR, "p#permanentAddress") # //p[@id='permanentAddress']

    #button
    SUBMIT = (By.CSS_SELECTOR, "#submit")                               # //button[@id='submit']