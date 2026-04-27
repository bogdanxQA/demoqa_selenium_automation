from selenium.webdriver.common.by import By

class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, "#demo-tab-what")
    WHAT_TAB_CONTENT = (By.CSS_SELECTOR, "#demo-tabpane-what p")
    ORIGIN_TAB = (By.CSS_SELECTOR, "#demo-tab-origin")
    ORIGIN_TAB_CONTENT = (By.CSS_SELECTOR, "#demo-tabpane-origin p")
    USE_TAB = (By.CSS_SELECTOR, "#demo-tab-use")
    USE_TAB_CONTENT = (By.CSS_SELECTOR, "#demo-tabpane-use p")
    MORE_TAB = (By.CSS_SELECTOR, "#demo-tab-more")
    MORE_TAB_CONTENT = (By.CSS_SELECTOR, "#demo-tabpane-more p")


