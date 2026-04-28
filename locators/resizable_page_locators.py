from selenium.webdriver.common.by import By

class ResizablePageLocators:
    RESIZABLE_BOX_WITH_BOUNDARIES = (By.CSS_SELECTOR, "#resizableBoxWithRestriction")
    HANDLE = (By.CSS_SELECTOR, ".react-resizable-handle.react-resizable-handle-se")
    RESIZABLE_WO_BOUNDARIES = (By.CSS_SELECTOR, "#resizable")

