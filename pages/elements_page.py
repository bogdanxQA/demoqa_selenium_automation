from locators.text_box_page_locators import TextBoxPageLocators
from locators.check_box_page_locators import CheckBoxPageLocators
from locators.radio_button_page_locators import RadioButtonPageLocators
from pages.base_page import BasePage
import time
from data.genarator.genarator import person_genarated
import random


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_inputs(self):
        person_info = next(person_genarated())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_created_form(self):
        full_name = self.element_is_present(self.locators.NAME_CREATED).text.split(':')[1]
        email = self.element_is_present(self.locators.EMAIL_CREATED).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CURRENT_ADDRESS_CREATED).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.PERMANENT_ADDRESS_CREATED).text.split(':')[1]
        return full_name, email, current_address, permanent_address
    

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()
    #Открываю все свитчеры
    def open_full_list(self):
        
        while True:
            closed_tree_switcher = self.driver.find_elements(*self.locators.TREE_SWITCHER)
            if not closed_tree_switcher:
                break
            closed_tree_switcher[0].click()


    def random_click_to_checkbox(self):
        items = self.elements_are_visible(self.locators.CHECK_BOX)
        item = items[random.randint(2,15)]
        self.scroll_to_element(item)
        item.click()
        
    def get_selected_checkbox_labels(self):
        elements  = self.elements_are_presents(self.locators.aria_checked)
        lables = []
        for element in elements:
            lables.append(element.get_attribute('aria-label').split()[1].lower()) 
        return lables    
    
    def get_displayed_selected_values(self):
        elements = self.elements_are_presents(self.locators.text_success)
        values = []
        for element in elements:
            values.append(element.text) 
        return values 
    
class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    def click_to_radio_button_yes(self):
        element = self.element_is_present(self.locators.YES_RADIO)
        element.click()

    def click_to_radio_button_impressive(self):
        element = self.element_is_present(self.locators.IMPRESSIVE_RADIO)
        element.click()    

    def get_displayed_selected_button(self):
        return self.element_is_present(self.locators.TEXT_SUCCSESS).text
    
    # def get_selected_radio_button_value(self):
    #     return self.find_element(self.locators.BUTTON_YES_TEXT).text

    

        
        
            

        
        