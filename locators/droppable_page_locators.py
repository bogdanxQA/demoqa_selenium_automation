from selenium.webdriver.common.by import By


class DroppablePageLocators():

    SIMPLE_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-simple")
    DRAGGABLE = (By.CSS_SELECTOR, "#draggable")
    DROPPABLE = (By.CSS_SELECTOR, "#simpleDropContainer #droppable")
    

    ACCEPT_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-accept")
    ACCEPTABLE_DRAG = (By.CSS_SELECTOR, "#acceptable")
    NOT_ACCEPTABLE_DRAG = (By.XPATH, "//div[text()='Not Acceptable']")
    ACCEPTABLE_DROP = (By.CSS_SELECTOR, "#acceptDropContainer div[class*='drop-box']")
    ACCEPTABLE_DROP_ACTIVE = (By.CSS_SELECTOR, "#acceptDropContainer div[class='drop-box ui-droppable ui-droppable-active ui-active']")

    PREVENT_PROPOGATION_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-preventPropogation")
    PREVENT_DRAG = (By.CSS_SELECTOR, "#dragBox")
    NOT_GREEDY_OUTER_DROP_BOX = (By.CSS_SELECTOR, "#notGreedyDropBox")
    NOT_GREEDY_INNER_DROP_BOX = (By.CSS_SELECTOR, "#notGreedyInnerDropBox")
    GREEDY_OUTER_DROP_BOX = (By.CSS_SELECTOR, "#greedyDropBox")
    GREEDY_INNER_DROP_BOX = (By.CSS_SELECTOR, "#greedyDropBoxInner")
    ACTIVE_NOT_GREEDY_DROP_BOX = (By.CSS_SELECTOR, "#notGreedyDropBox div[class='drop-box ui-droppable ui-droppable-active ui-active']")

    REVERT_DRAGGABLE_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-revertable")
    REVERTABLE_DRAG = (By.CSS_SELECTOR, "#revertable")
    NOT_REVERTABLE_DRAG = (By.CSS_SELECTOR, "#notRevertable")
    DROB_BOX_REVERT = (By.CSS_SELECTOR, "#revertableDropContainer #droppable")
    REVERT_ITEM_AFTER_DROP = (By.CSS_SELECTOR, "#revertable[style= 'position: relative; left: 0px; top: 0px;']")
    NOT_REVERT_ITEM_AFTER_DROP = (By.CSS_SELECTOR, "#notRevertable.drag-box.mt-4.ui-draggable.ui-draggable-handle")
    ACTIVE_DROP_BOX_REVERT = (By.CSS_SELECTOR, "#revertableDropContainer #droppable.drop-box.ui-droppable.ui-droppable-active,ui-active")


