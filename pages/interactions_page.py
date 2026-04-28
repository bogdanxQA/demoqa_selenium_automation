from pages.base_page import BasePage
from locators.sortable_page_locators import SortablePageLocators
from locators.selectable_page_locators import SelectablePageLocators
from locators.resizable_page_locators import ResizablePageLocators
import random
import time


class SortablePage(BasePage):


    locators = SortablePageLocators()

    def move_random_elements_in_list(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        elements_before = self.elements_are_presents(self.locators.LIST_ITEMS)
        item_list_before = [element.text for element in elements_before]
        moved_elements = random.sample(item_list_before, 2)

        what = self.wait_for_element_text_in_list(self.locators.LIST_ITEMS, moved_elements[0])
        where = self.wait_for_element_text_in_list(self.locators.LIST_ITEMS, moved_elements[1])
        
        self.drag_and_drop_with_offset(what, where, 5)
                
        elements_after = self.elements_are_presents(self.locators.LIST_ITEMS)
        item_list_after = [element.text for element in elements_after]
        return item_list_before, item_list_after
    
    def move_random_elements_in_grid(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        elements_before = self.wait_for_elements_to_have_text(self.locators.GRID_ITEMS)
        item_list_before = [element.text for element in elements_before]
        moved_elements = random.sample(item_list_before, 2)

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
      Потому что проверяю именно возможно выбора элемента"""
    def select_random_inactive_items_in_list(self):
        
        self.element_is_visible(self.locators.LIST_TAB).click()
        
        all_items = self.wait_for_elements_to_have_text(self.locators.LIST_ITEMS)
        
        inactive_items = [el for el in all_items if 'active' not in el.get_attribute('class')]
        if not inactive_items:
            return []  
        k = random.randint(1, len(inactive_items))
        chosen_items = random.sample(inactive_items, k)
        selected_items = [item.text for item in chosen_items]
        
        for item in chosen_items:
            item.click()
        
        return selected_items
    
    def get_active_items_in_list(self):
        active_items = self.elements_are_presents(self.locators.ACTIVE_LIST_ITEMS)
        return [item.text for item in active_items]
    

    def select_random_inactive_items_in_grid(self):
        
        self.element_is_visible(self.locators.GRID_TAB).click()
        
        all_items = self.wait_for_elements_to_have_text(self.locators.GRID_ITEMS)
        
        inactive_items = [el for el in all_items if 'active' not in el.get_attribute('class')]
        if not inactive_items:
            return []  
        k = random.randint(1, len(inactive_items))
        chosen_items = random.sample(inactive_items, k)
        selected_items = [item.text for item in chosen_items]
        
        for item in chosen_items:
            item.click()
        
        return selected_items
    
    def get_active_items_in_grid(self):
        active_items = self.elements_are_presents(self.locators.ACTIVE_GRID_ITEMS)
        return [item.text for item in active_items]


class ResizablePage(BasePage):

    locators = ResizablePageLocators()

    def change_size_in_resizable_box_with_boundaries(self):
        resizable_box = self.element_is_present(self.locators.RESIZABLE_BOX_WITH_BOUNDARIES)
        
        handle = self.elements_are_visible(self.locators.HANDLE)[0]
        
        time.sleep(0.5) #Либо на этом сайте элементы не стабильны, либо мне не хватает знаний. Можно написать в BasePage метод универсальный, который дожидается стабильности элемента, но он тоже будет использовать time.sleep
        self.drag_and_drop_by_offset(handle, 500, 500)
        max_size = self.get_width_and_height(resizable_box)
        self.drag_and_drop_by_offset(handle, -350, -350)
        min_size = self.get_width_and_height(resizable_box)
        return max_size, min_size
        


    def get_width_and_height(self, element):
        before = element.get_attribute("style")
        width = before.split("width: ")[1].split(";")[0].strip()
        height = before.split("height: ")[1].split(";")[0].strip()
        return [width, height]
    
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



