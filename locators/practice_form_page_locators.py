from selenium.webdriver.common.by import By

class PracticeFormPageLocators:
                                                                                    #xpath:
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")                                    # //input[@id="firstName"]
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")                                      # //input[@id="lastName"]    
    EMAIL = (By.CSS_SELECTOR, "#userEmail")                                         # //input[@id="userEmail"]
    MALE_RADIO_BUTTON = (By.CSS_SELECTOR, "input[value='Male']")                    # //input[@value="Male"]                         Также можнно MALE_RADIO_BUTTON = (By.CSS_SELECTOR, f"div[id='genterWrapper'] input[id='gender-radio-{random.randint(1,3)}']")
    FEMALE_RADIO_BUTTON = (By.CSS_SELECTOR, "input[value='Female']")                # //input[@value="Female"]
    OTHER_RADIO_BUTTON = (By.CSS_SELECTOR, "input[value='Other']")                  # //input[@value="Other"]
    MOBILE_NUMBER = (By.CSS_SELECTOR, "#userNumber")                                # //input[@id='userNumber']
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "#dateOfBirthInput")                          # //input[@id='dateOfBirthInput']
    SUBJECTS = (By.CSS_SELECTOR, "#subjectsInput")                                  # //input[@id='subjectsInput']
    SPORTS_CHECKBOX = (By.CSS_SELECTOR, "#hobbies-checkbox-1")                      # //input[@id='hobbies-checkbox-1']
    READING_CHECKBOX = (By.CSS_SELECTOR, "#hobbies-checkbox-2")                     # //input[@id='hobbies-checkbox-2']
    MUSIC_CHECKBOX = (By.CSS_SELECTOR, "#hobbies-checkbox-3")                       # //input[@id='hobbies-checkbox-3']
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "#uploadPicture")                             # //input[@id='uploadPicture']
    CURRENT_ADRESS = (By.CSS_SELECTOR, "#currentAddress")                           # //input[@id='currentAddress']
    SELECTOR_STATE_INPUT = (By.CSS_SELECTOR, "#react-select-3-input")               # //input[@id='react-select-3-input']
    SELECTOR_STATE_ID = (By.CSS_SELECTOR, "div[id='state']")                        # //div[@id='state']
    SELECTOR_CITY_ID = (By.CSS_SELECTOR, "div[id='city']")
    SELECTOR_CITY_INPUT = (By.CSS_SELECTOR, "#react-select-4-input")
    STATE_AND_CITY_TEXT = (By.CSS_SELECTOR, "div[class='css-1dimb5e-singleValue']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")                                    # //button[@id='submit']
    


    DISPLAYED_DATA = (By.XPATH, "//div[@class='modal-content']//tbody/tr")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "#closeLargeModal")
    MODAL_CONTENT = (By.CSS_SELECTOR, "div[class='modal-content']")
