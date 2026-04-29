from selenium.webdriver.common.by import By


class ProgressBarPageLocators:

    START_STOP_BUTTON = (By.CSS_SELECTOR, "#startStopButton")
    RESET_BUTTON = (By.CSS_SELECTOR, "#resetButton")
    PROGRESS_BAR = (By.CSS_SELECTOR, "#progressBar")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "#progressBar [role='progressbar']")
    

