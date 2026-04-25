from selenium.webdriver.common.by import By


class AlertsPageLocators:                                                       #xpath:
    ALERT_BUTTON = (By.CSS_SELECTOR, "#alertButton")                            # //button[@id = 'alertButton']      
    ALERT_AFTER_TIME_BUTTON = (By.CSS_SELECTOR, "#timerAlertButton")            # //button[@id = 'timerAlertButton']
    CONFIRM_BOX_BUTTON = (By.CSS_SELECTOR, "#confirmButton")                    # //button[@id = 'confirmButton']  
    PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, "#promtButton")                       # //button[@id = 'promtButton'] 
    RESULT_CONFIRM_BUTTON = (By.CSS_SELECTOR, "#confirmResult")                 # //span[@id='confirmResult']    
    RESULT_PROMPT_BUTTON = (By.CSS_SELECTOR, "#promptResult")                   # //span[@id='promptResult']   

    
