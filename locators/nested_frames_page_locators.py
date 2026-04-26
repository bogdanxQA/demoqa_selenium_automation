from selenium.webdriver.common.by import By


class NestedFramesPageLocators:

    PARENT_FRAME = (By.CSS_SELECTOR, "#frame1")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    FRAME_TEXT = (By.CSS_SELECTOR, "body")
    