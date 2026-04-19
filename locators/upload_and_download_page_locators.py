from selenium.webdriver.common.by import By


class DownloadAndUploadPageLocators:                                                         #xpath:
    DOWNLOAD_BTN = (By.CSS_SELECTOR, "#downloadButton")                                      # //a[@id = 'downloadButton']      
    UPLOAD_BTN = (By.CSS_SELECTOR, "#uploadFile")                                            # //input[@id = 'uploadFile']
    UPLOAD_PATH = (By.CSS_SELECTOR, "#uploadedFilePath")                                     # //input[@id = 'uploadedFilePath']
