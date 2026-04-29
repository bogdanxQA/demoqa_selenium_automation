from pages.base_page import BasePage
from locators.sortable_page_locators import SortablePageLocators
from locators.selectable_page_locators import SelectablePageLocators
from locators.resizable_page_locators import ResizablePageLocators
from locators.droppable_page_locators import DroppablePageLocators
from locators.dragabble_page_locators import DragabblePageLocators
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from typing import Literal
import allure


class SortablePage(BasePage):


    locators = SortablePageLocators()

    @allure.step("Move random element in list")
    def move_random_elements_in_list(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        elements_before = self.elements_are_presents(self.locators.LIST_ITEMS)
        item_list_before = [element.text for element in elements_before]
        moved_elements = random.sample(item_list_before, 2)
        with allure.step(f"Select elements to move: {moved_elements}"):
            what = self.wait_for_element_text_in_list(self.locators.LIST_ITEMS, moved_elements[0])
            where = self.wait_for_element_text_in_list(self.locators.LIST_ITEMS, moved_elements[1])
        self.drag_and_drop_with_offset(what, where, 5)
        elements_after = self.elements_are_presents(self.locators.LIST_ITEMS)
        item_list_after = [element.text for element in elements_after]
        return item_list_before, item_list_after
    
    @allure.step("Move random element in grid")
    def move_random_elements_in_grid(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        elements_before = self.wait_for_elements_to_have_text(self.locators.GRID_ITEMS)
        item_list_before = [element.text for element in elements_before]
        moved_elements = random.sample(item_list_before, 2)
        with allure.step(f"Select elements to move: {moved_elements}"):
            what = self.wait_for_element_text_in_list(self.locators.GRID_ITEMS, moved_elements[0])
            where = self.wait_for_element_text_in_list(self.locators.GRID_ITEMS, moved_elements[1])
        self.drag_and_drop_with_offset(what, where, 5)
        elements_after = self.elements_are_presents(self.locators.GRID_ITEMS)
        item_list_after = [element.text for element in elements_after]
        return item_list_before, item_list_after
    
class SelectablePage(BasePage):

    locators = SelectablePageLocators()

    """Если есть условие, что изначально все items неактивны, то делать отдельный список неактивных элементов излишне.
      Я немного улучшил метод, в случае, если изначально какой-то item уже будет выбран.
      Потому что проверяю именно возможность выбора элемента"""
    @allure.step("Select random inactive items in list")
    def select_random_inactive_items_in_list(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        all_items = self.wait_for_elements_to_have_text(self.locators.LIST_ITEMS)
        inactive_items = [el for el in all_items if 'active' not in el.get_attribute('class')]

        if not inactive_items:
            return []  
        k = random.randint(1, len(inactive_items))
        chosen_items = random.sample(inactive_items, k)
        selected_items = [item.text for item in chosen_items]
        with allure.step(f"Click on selected items: {selected_items}"):
            for item in chosen_items:
                item.click()
        
        return selected_items
    
    @allure.step("Get active items in list")
    def get_active_items_in_list(self):
        active_items = self.elements_are_presents(self.locators.ACTIVE_LIST_ITEMS)
        return [item.text for item in active_items]
    
    @allure.step("Select random inactive items in grid")
    def select_random_inactive_items_in_grid(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        all_items = self.wait_for_elements_to_have_text(self.locators.GRID_ITEMS)
        inactive_items = [el for el in all_items if 'active' not in el.get_attribute('class')]
        if not inactive_items:
            return []  
        k = random.randint(1, len(inactive_items))
        chosen_items = random.sample(inactive_items, k)
        selected_items = [item.text for item in chosen_items]
        
        with allure.step(f"Click on selected grid items: {selected_items}"):
            for item in chosen_items:
                item.click()
        return selected_items
    
    @allure.step("Get active items in grid")
    def get_active_items_in_grid(self):
        active_items = self.elements_are_presents(self.locators.ACTIVE_GRID_ITEMS)
        return [item.text for item in active_items]


class ResizablePage(BasePage):

    locators = ResizablePageLocators()

    @allure.step("Change size of element in box with boundaries")
    def change_size_in_resizable_box_with_boundaries(self):
        resizable_box = self.element_is_present(self.locators.RESIZABLE_BOX_WITH_BOUNDARIES)
        
        handle = self.elements_are_visible(self.locators.HANDLE)[0]
        with allure.step("Wait for handle stabilisation"):
            time.sleep(0.5) #Либо на этом сайте элементы не стабильны, либо мне не хватает знаний. Можно написать в BasePage метод универсальный, который дожидается стабильности элемента, но он тоже будет использовать time.sleep
        self.drag_and_drop_by_offset(handle, 500, 500)
        max_size = self.get_width_and_height(resizable_box)
        self.drag_and_drop_by_offset(handle, -350, -350)
        min_size = self.get_width_and_height(resizable_box)
        return max_size, min_size
        

    @allure.step("Get width and height")
    def get_width_and_height(self, element):
        before = element.get_attribute("style")
        width = before.split("width: ")[1].split(";")[0].strip()
        height = before.split("height: ")[1].split(";")[0].strip()
        return [width, height]
    
    @allure.step("Change size of element without boundaries")
    def change_size_in_resizable_wo_boundaries(self):
        resizable = self.element_is_present(self.locators.RESIZABLE_WO_BOUNDARIES)
        start_size = self.get_width_and_height(resizable)
        handle = self.elements_are_visible(self.locators.HANDLE)[1]
        time.sleep(0.5)
        self.drag_and_drop_by_offset(handle, random.randint(1, 400), random.randint(1, 400))
        increased_size = self.get_width_and_height(resizable)
        self.drag_and_drop_by_offset(handle, -500, -500)
        min_size = self.get_width_and_height(resizable)
        return start_size, increased_size, min_size
    
class DroppablePage(BasePage):

    locators = DroppablePageLocators()

    @allure.step("Get text and hex color after drop")
    def drag_and_drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_me = self.element_is_visible(self.locators.DRAGGABLE)
        drop_here = self.element_is_visible(self.locators.DROPPABLE)
        
        self.drag_and_drop_elements(drag_me, drop_here)
        res = drop_here.text
        rgba_color = drop_here.value_of_css_property("background-color")
        hex_color = Color.from_string(rgba_color).hex
        return res, hex_color
    
    @allure.step("Get hex colors before, after hold and drop, and get text after drop")
    def drag_and_drop_acceptable(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable = self.element_is_visible(self.locators.ACCEPTABLE_DRAG)
        drop = self.element_is_visible(self.locators.ACCEPTABLE_DROP)
        hex_color_before = Color.from_string(drop.value_of_css_property("background-color")).hex
        hex_color_after_click_and_hold = self.drag_wo_drop(source=acceptable, active_drop_locator=self.locators.ACCEPTABLE_DROP_ACTIVE)
        self.drag_and_drop_elements(acceptable, drop)
        res = drop.text
        hex_color_after_drop = Color.from_string(drop.value_of_css_property("background-color")).hex
        return hex_color_before, hex_color_after_click_and_hold, hex_color_after_drop, res

    @allure.step("Do drag without drop and get hex color")
    def drag_wo_drop(self, source, active_drop_locator):
        action = ActionChains(self.driver)
        action.click_and_hold(source).pause(0.2).move_by_offset(5,5).pause(0.5).perform()
        
        active_drop = self.element_is_present(active_drop_locator)
        hex_color_after_click_and_hold = Color.from_string(active_drop.value_of_css_property("background-color")).hex
        action.release().perform()
        return hex_color_after_click_and_hold
    
    @allure.step("drag&drop not acceptable item and get text")
    def drag_and_drop_not_acceptable(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        not_acceptable = self.element_is_visible(self.locators.NOT_ACCEPTABLE_DRAG)
        drop = self.element_is_visible(self.locators.ACCEPTABLE_DROP)
        self.drag_and_drop_elements(not_acceptable, drop)
        return drop.text
    
    
    def _drag_and_drop_common(self, outer_drop_locator, inner_drop_locator, where, is_greedy=False):
        with allure.step("Switch to Prevent Propagation tab"):
            self.element_is_visible(self.locators.PREVENT_PROPOGATION_TAB).click()
        prevent_drag = self.element_is_visible(self.locators.PREVENT_DRAG)
        outer_drop = self.element_is_visible(outer_drop_locator)
        inner_drop = self.element_is_visible(inner_drop_locator)
        
        with allure.step("Capture initial color and perform drag without drop (click and hold)"):
            hex_color_before = Color.from_string(outer_drop.value_of_css_property("background-color")).hex
            hex_color_after_click_and_hold = self.drag_wo_drop(
                source=prevent_drag,
                active_drop_locator=self.locators.ACTIVE_NOT_GREEDY_DROP_BOX
            )
        
        if where == "outer":
            with allure.step("Drag and drop to OUTER zone"):
                self.drag_and_drop_elements_with_offset(prevent_drag, outer_drop, 0, -90)
                hex_color_after_drop = Color.from_string(outer_drop.value_of_css_property("background-color")).hex
                res_outer = outer_drop.text.splitlines()
            return hex_color_before, hex_color_after_click_and_hold, hex_color_after_drop, res_outer
        else: 
            with allure.step("Drag and drop to INNER zone"): 
                self.drag_and_drop_elements(prevent_drag, inner_drop)
                hex_color_outer_after_drop = Color.from_string(outer_drop.value_of_css_property("background-color")).hex
                res_outer = outer_drop.text.splitlines()
            if is_greedy:
                with allure.step("Get INNER drop zone color after drop (greedy)"):
                    hex_color_inner_after_drop = Color.from_string(inner_drop.value_of_css_property("background-color")).hex
                return hex_color_before, hex_color_after_click_and_hold, hex_color_outer_after_drop, hex_color_inner_after_drop, res_outer
            else:
                return hex_color_before, hex_color_after_click_and_hold, hex_color_outer_after_drop, res_outer

    
    def drag_and_drop_not_greedy_box(self, where: Literal["inner", "outer"]):
        return self._drag_and_drop_common(
            self.locators.NOT_GREEDY_OUTER_DROP_BOX,
            self.locators.NOT_GREEDY_INNER_DROP_BOX,
            where,
            is_greedy=False
        )

    def drag_and_drop_greedy_box(self, where: Literal["inner", "outer"]):
        return self._drag_and_drop_common(
            self.locators.GREEDY_OUTER_DROP_BOX,
            self.locators.GREEDY_INNER_DROP_BOX,
            where,
            is_greedy=True
        )
    

    
    def drag_and_drop_revert_and_not_revert_item(self, which: Literal["revert", "not_revert"]):
        self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB).click()
        drop_box = self.element_is_visible(self.locators.DROB_BOX_REVERT)

        if which == "revert":
            with allure.step("Drag and drop revertable item"):
                drag_item = self.element_is_visible(self.locators.REVERTABLE_DRAG)
                after_drop_locator = self.locators.REVERT_ITEM_AFTER_DROP
        else:
            with allure.step("Drag and drop not revertable item"):
                drag_item = self.element_is_visible(self.locators.NOT_REVERTABLE_DRAG)
                after_drop_locator = self.locators.NOT_REVERT_ITEM_AFTER_DROP

        self.drag_and_drop_elements(drag_item, drop_box)
        self.element_is_present(after_drop_locator)  

        
        position_after_move = drag_item.get_attribute("style")
        left = position_after_move.split("left: ")[1].split(";")[0]
        top = position_after_move.split("top: ")[1].split(";")[0]

        return left, top, drop_box.text


class DragabblePage(BasePage):

    locators = DragabblePageLocators()

    @allure.step("Get element location before and after move")
    def get_element_location_before_and_after_move(self, element):

        position_before = element.location
        x = random.randint(20, 50)
        y = random.randint(20, 50)
        with allure.step(f"Drag element by offset ({x}, {y})"):
            self.drag_and_drop_by_offset(element, x, y)
        position_after = element.location
        return position_after, position_before
    
    allure.step("Get drag box position after and before drop (simple tab)")
    def simple_drag_box(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_box = self.element_is_visible(self.locators.DRAG_BOX_SIMPLE)
        position_after, position_before = self.get_element_location_before_and_after_move(drag_box)
        return position_after, position_before
    
    allure.step("Get axis restricted drag box position before and after")
    def axis_restricted_drag_box(self, which: Literal["only_x", "only_y"]):
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()

        if which == "only_x":
            with allure.step("Use only X axis drag box"):
                drag_box = self.element_is_visible(self.locators.DRAG_BOX_ONLY_X)
            
        elif which == "only_y":
            with allure.step("Use only Y axis drag box"):
                drag_box = self.element_is_visible(self.locators.DRAG_BOX_ONLY_Y)

        position_after, position_before = self.get_element_location_before_and_after_move(drag_box)
        return position_after, position_before
    

    allure.step("Drag and drop item in box with bounds")
    def drag_and_drop_with_bounds(self, x_offset=500, y_offset=500):
        self.element_is_visible(self.locators.CONTAINER_RESTRICTED_TAB).click()
        draggable = self.element_is_visible(self.locators.CONTAINED_DRAG_BOX)
        container = self.element_is_visible(self.locators.CONTAINER)
        cont_rect = container.rect
        left, top = cont_rect['x'], cont_rect['y']
        right = left + cont_rect['width']
        bottom = top + cont_rect['height']

        start = draggable.location
        with allure.step(f"Drag element by offset ({x_offset}, {y_offset})"):
            self.drag_and_drop_by_offset(draggable, x_offset, y_offset)
        end = draggable.location
        size = draggable.size


        return {
        'start': start,
        'end': end,
        'size': size,
        'bounds': (left, top, right, bottom)
    }
            



        
        

    

            








