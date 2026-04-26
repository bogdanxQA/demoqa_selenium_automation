from selenium.webdriver.common.by import By

class AccodrianPageLocators:

    ACCORDIAN_BUTTON = (By.CSS_SELECTOR, "button[type='button'][aria-expanded]")
    # ACCORDIAN_CONTENT = (By.CSS_SELECTOR, f".accordion-item:nth-child({number+1}) .accordion-body p")
    ACCORDIAN_CONTENT = (By.XPATH, "//div[@class='accordion-body']//p")
    