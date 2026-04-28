from selenium.webdriver.common.by import By

class SelectablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, "#demo-tab-list")
    GRID_TAB = (By.CSS_SELECTOR, "#demo-tab-grid")
    LIST_ITEMS = (By.CSS_SELECTOR, "li[class = 'mt-2 list-group-item list-group-item-action']")
    ACTIVE_LIST_ITEMS = (By.CSS_SELECTOR, ".list-group-item.active")
    GRID_ITEMS = (By.CSS_SELECTOR, "li[class = 'list-group-item list-group-item-action']")
    ACTIVE_GRID_ITEMS = (By.CSS_SELECTOR, ".list-group-item.active")

