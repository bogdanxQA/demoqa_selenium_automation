from selenium.webdriver.common.by import By


class RadioButtonPageLocators:                                                  #xpath:
    YES_RADIO = (By.CSS_SELECTOR, "#yesRadio")                                  # //input[@id = 'yesRadio']    
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "#impressiveRadio")                    # //input[@id = 'impressiveRadio']   
    TEXT_SUCCSESS = (By.CSS_SELECTOR, ".text-success")                           # //span[@class='text-success'] 
    BUTTON_YES_TEXT = (By.CSS_SELECTOR, "label[for='yesRadio']")                # //label[@for='yesRadio']
    BUTTON_IMPRESSIVE_TEXT = (By.CSS_SELECTOR, "label[for='impressiveRadio']")  # //label[@for='impressiveRadio']     
 



                                                                        
