from selenium.webdriver.common.by import By


class WebTablesPageLocators():
                                                                                    #xpath:
    ADD = (By.CSS_SELECTOR, "#addNewRecordButton")                                  # //button[@id='addNewRecordButton']                       
    SEARCH_BOX = (By.CSS_SELECTOR, "#searchBox")                                    # //input[@id='searchBox']
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")                                    # //input[@id='firstName']
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")                                      # //input[@id='lastName']
    EMAIL = (By.CSS_SELECTOR, "#userEmail")                                         # //input[@id='userEmail']   
    AGE = (By.CSS_SELECTOR, "#age")                                                 # //input[@id='age']
    SALARY = (By.CSS_SELECTOR, "#salary")                                           # //input[@id='salary']
    DEPARTMENT = (By.CSS_SELECTOR, "#department")                                   # //input[@id='department']
    SHOW = (By.CSS_SELECTOR, "select.form-control")                                 # //select[@class = 'form-control']
    DELETE = (By.CSS_SELECTOR, "span[title='Delete']")                              # //span[@title='Delete']
    SUBMIT = (By.CSS_SELECTOR, "#submit")
    TABLE_BODY = (By.CSS_SELECTOR, "tbody tr")    
    TEXT_TABLE_BODY = (By.TAG_NAME, "td")          
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")         
    SHOW_ROWS_SELECT = (By.CSS_SELECTOR, "select.form-control")                  
