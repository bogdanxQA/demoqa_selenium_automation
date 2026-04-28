from selenium.webdriver.common.by import By

class SortablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, "#demo-tab-list")
    GRID_TAB = (By.CSS_SELECTOR, "#demo-tab-grid")
    LIST_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-list [class='list-group'] [class='list-group-item list-group-item-action']")
    GRID_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-grid [class='create-grid'] [class='list-group-item list-group-item-action']")

