from locators.text_box_page_locators import TextBoxPageLocators
from locators.check_box_page_locators import CheckBoxPageLocators
from locators.radio_button_page_locators import RadioButtonPageLocators
from locators.web_tables_page_locators import WebTablesPageLocators
from locators.buttons_page_locators import ButtonsPageLocators
from locators.links_page_locators import LinksPageLocators
from locators.upload_and_download_page_locators import DownloadAndUploadPageLocators
from locators.dynamic_propetries_page_locators import DynamicPropertiesPageLocators
from pages.base_page import BasePage
import time
from data.generator.generator import person_genarated, data_genarated, file_generated
import random
from selenium.webdriver.support.select import Select 
import requests
import os





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
            #self.scroll_to_element(select_element)
            select = Select(select_element)
            select.select_by_value(str(value))


"""Ничего не помогло кроме time.sleep() - не знаю что делать, оставлю костыль"""
class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def double_click_on_btn(self):
        time.sleep(0.1)
        self.double_click(self.element_is_clickable(self.locators.DOUBLE_CLICK_BUTTON))
        return self.checked_res_clicked_on_the_btn(self.locators.DOUBLE_CLICK_MSG)


    def right_click_on_btn(self):
        time.sleep(0.1)
        self.right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.checked_res_clicked_on_the_btn(self.locators.RIGHT_CLICK_MSG)
    
    def click_on_click_me_button(self):
        time.sleep(0.1)
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
        return self.checked_res_clicked_on_the_btn(self.locators.CLICK_ME_MSG)


    


    def checked_res_clicked_on_the_btn(self, element):
        return self.element_is_visible(element).text
"""Предположил, что нужно взять ссылку из запроса и сравнить с ожидаемым статус кодом. Возможно придется переделать. В целом коряво."""    
class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link = simple_link.get_attribute('href')
        request = requests.get(link)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link, url
        else:
            return link, request.status_code 
        

    def check_not_found_link(self):
        request = requests.get("https://demoqa.com/invalid-url")
        if request.status_code == 200:
            self.element_is_present(self.locators.NOT_FOUND_LINK).click()
        else:
            return request.status_code


  

class DownloadAndUploadPage(BasePage):
    locators = DownloadAndUploadPageLocators()


    def download_file(self):
        pass

    """Генерируем файл, загружаем, удаляем, проверяем"""
    def upload_file(self):
        file_name, path = file_generated()
        self.element_is_present(self.locators.UPLOAD_BTN).send_keys(path)
        displayed_path = self.element_is_visible(self.locators.UPLOAD_PATH).text
        os.remove(path)
        assert file_name in displayed_path

class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def click_to_will_enable_btn(self):
        try:
            self.element_is_clickable(self.locators.WILL_ENABLE_BUTTON).click()
        except:
            return False
        return True

    def click_to_visible_after_btn(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON).click()
        except:
            return False
        return True
        

    """Чтобы не ставить time.sleep установил каунтер. Кнопка меняет цвет вместе с появлением другой кнопки"""
    def check_color_change_btn(self):
        element = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        element_before = element.value_of_css_property('color')
        self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        element_after = element.value_of_css_property('color')
        return element_before, element_after
        

    def get_text_with_random_id(self):
        element = self.element_is_visible(self.locators.RANDOM_ID_TEXT)
        return element.text

    



        
 


    

        
        
            

        
        