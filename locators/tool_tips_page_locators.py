from selenium.webdriver.common.by import By

class ToolTipsPageLocators:
    HOVER_ME_BUTTON = (By.CSS_SELECTOR, "#toolTipButton")
    AFTER_HOVER_BUTTON = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")
    HOVER_ME_INPUT = (By.CSS_SELECTOR, "#toolTipTextField")
    AFTER_HOVER_INPUT = (By.CSS_SELECTOR, "input[aria-describedby='textFieldToolTip']")
    HOVER_CONTENT = (By.CSS_SELECTOR, "div[class='tooltip-inner']")
    HOVER_CONTRARY = (By.XPATH, "//a[text()='Contrary']")
    AFTER_HOVER_CONTRARY = (By.CSS_SELECTOR, "a[aria-describedby='contraryTexToolTip']")
    HOVER_TEXT = (By.XPATH, "//a[text()='1.10.32']")
    AFTER_HOVER_TEXT = (By.CSS_SELECTOR, "a[aria-describedby='sectionToolTip']")
                     


    
    