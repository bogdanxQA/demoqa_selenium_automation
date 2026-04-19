from locators.text_box_page_locators import TextBoxPageLocators
from locators.check_box_page_locators import CheckBoxPageLocators
from locators.radio_button_page_locators import RadioButtonPageLocators
from locators.web_tables_page_locators import WebTablesPageLocators
from pages.base_page import BasePage
import time
from data.genarator.genarator import person_genarated, data_genarated
import random
from selenium.webdriver.support.select import Select 


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

    def click_to_radio_button_no(self):
        element = self.element_is_present(self.locators.NO_RADIO)
        element.click()  

    def get_displayed_selected_button(self):
        return self.element_is_present(self.locators.TEXT_SUCCSESS).text
    
    # def get_selected_radio_button_value(self):
    #     return self.find_element(self.locators.BUTTON_YES_TEXT).text


class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    """Меняя count можно создать =count кол-во тестовых данных"""
    def add_new_data(self,count=1):
        new_data = []        
        while count!=0:
            self.element_is_clickable(self.locators.ADD).click()
            data = next(data_genarated())
            first_name = data.first_name
            last_name = data.last_name
            email = data.email
            age = data.age
            salary = data.salary
            department = data.department
        
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.AGE).send_keys(age)
            self.element_is_visible(self.locators.SALARY).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
            
            self.element_is_visible(self.locators.SUBMIT).click()
            new_data.append(f"{first_name} {last_name} {age} {email} {salary} {department}")
            count = count - 1
        return new_data
    
    def get_full_data(self):
            elements = self.elements_are_presents(self.locators.TABLE_BODY)
            all_data = []
            for element in elements:
                a = element.find_elements(*self.locators.TEXT_TABLE_BODY)
                first_name = a[0].text
                last_name = a[1].text
                age = a[2].text
                email = a[3].text
                salary = a[4].text
                department = a[5].text
                final = f"{first_name} {last_name} {age} {email} {salary} {department}"
                all_data.append(final)
            return all_data
    
    def search_box_clear_and_send_keys(self, send_keys:str):
        element = self.element_is_present(self.locators.SEARCH_BOX)
        element.clear()
        time.sleep(0.5)
        element.send_keys(send_keys)
        return element.get_attribute("value")
    
    def update_data(self):
        element = self.elements_are_visible(self.locators.UPDATE_BUTTON)[0]
        data = next(data_genarated())
        age = data.age
        element.click()
        age_clear = self.element_is_visible(self.locators.AGE)
        age_clear.clear()
        age_clear.send_keys(age)
        
        self.element_is_visible(self.locators.SUBMIT).click()
        
        return {'age': str(age)}
    

    def delete_data(self):
        element = self.element_is_visible(self.locators.DELETE)
        element.click()




    def get_full_data_wo_wait(self):
            elements = self.driver.find_elements(*self.locators.TABLE_BODY)
            all_data = []
            for element in elements:
                a = element.find_elements(*self.locators.TEXT_TABLE_BODY)
                first_name = a[0].text
                last_name = a[1].text
                age = a[2].text
                email = a[3].text
                salary = a[4].text
                department = a[5].text
                final = f"{first_name} {last_name} {age} {email} {salary} {department}"
                all_data.append(final)
            return all_data


    
    def select_show_value(self, value = 50):
            select_element = self.element_is_visible(self.locators.SHOW_ROWS_SELECT)
            self.scroll_to_element(select_element)
            select = Select(select_element)
            select.select_by_value(str(value))
        
 


    

        
        
            

        
        