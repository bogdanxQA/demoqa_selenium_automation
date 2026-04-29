from selenium.webdriver.common.by import By


class DragabblePageLocators: 

    SIMPLE_TAB = (By.CSS_SELECTOR, "#draggableExample-tab-simple")
    DRAG_BOX_SIMPLE = (By.CSS_SELECTOR, "#dragBox")

    AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, "#draggableExample-tab-axisRestriction")
    DRAG_BOX_ONLY_X = (By.CSS_SELECTOR, "#restrictedX")
    DRAG_BOX_ONLY_Y = (By.CSS_SELECTOR, "#restrictedY")

    CONTAINER_RESTRICTED_TAB = (By.CSS_SELECTOR, "#draggableExample-tab-containerRestriction")
    CONTAINER = (By.CSS_SELECTOR, "#containmentWrapper")
    CONTAINED_DRAG_BOX = (By.CSS_SELECTOR, "#containmentWrapper [class *='draggable']")