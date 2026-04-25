from selenium.webdriver.common.by import By


class ModalDialogsPageLocators:                                                          #xpath:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "#showSmallModal")                            # //button[@id = 'showSmallModal']      
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "#showLargeModal")                            # //button[@id = 'showLargeModal']
    CLOSE_SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "#closeSmallModal")                     # //button[@id = 'closeSmallModal']
    CLOSE_LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "#closeLargeModal")                     # //button[@id = 'closeLargeModal']
    MODAL = (By.CSS_SELECTOR, "div[class='modal-content']")                              # //div[@class = 'modal-content']
