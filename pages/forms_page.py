from pages.base_page import BasePage
from locators.practice_form_page_locators import PracticeFormPageLocators
from data.generator.generator import practice_form_data_generated, file_generated
from data.data import SUBJECTS_LIST
from selenium.webdriver.common.keys import Keys
import random
import os


class PracticeFormPage(BasePage):

    locators = PracticeFormPageLocators()


    def fill_all_inputs(self):
         
        students_form = next(practice_form_data_generated())

        first_name = students_form.first_name #в return
        last_name = students_form.last_name #в return
        email = students_form.email #в return
        mobile_number = students_form.mobile_number #в return
        current_address = students_form.current_address #в return
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(mobile_number)
        self.element_is_visible(self.locators.CURRENT_ADRESS).send_keys(current_address)

        """Выбор рандомной радиокнопки + return value. Другой способ в локаторах"""
        gender_locators = [
             self.locators.MALE_RADIO_BUTTON,
             self.locators.FEMALE_RADIO_BUTTON,
             self.locators.OTHER_RADIO_BUTTON
        ]
        chosen_random_gender_locator = random.choice(gender_locators)
        random_gender_element = self.element_is_visible(chosen_random_gender_locator)
        chosen_gender_value = random_gender_element.get_attribute("value")   #в return
        random_gender_element.click()
     
        
                 
        """Выбор рандомных чекбоксов + return label"""
        check_box_locators = [
             (self.locators.SPORTS_CHECKBOX, "Sports"),
             (self.locators.MUSIC_CHECKBOX, "Music"),
             (self.locators.READING_CHECKBOX, "Reading")
        ]
        k = random.randint(1, len(check_box_locators))
        chosen_locators = random.sample(check_box_locators, k)
        selected_checkbox_values = []  #в return
        for locator, label in chosen_locators:
             self.element_is_visible(locator).click()
             selected_checkbox_values.append(label)


        file_name = self.upload_file()   #в return
        chosen_subjects = self.random_subject() #в return
        chosen_state = self.random_state() #в return
        chosen_city = self.random_city() #в return
        submit_button = self.element_is_visible(self.locators.SUBMIT_BUTTON)
        self.scroll_to_element(submit_button)
        submit_button.click()

        expected = {
    "first_name": first_name,
    "last_name": last_name,
    "email": email,
    "mobile": str(mobile_number),
    "gender": chosen_gender_value,
    "hobbies": selected_checkbox_values,    
    "subjects": chosen_subjects,            
    "file_name": file_name,
    "address": current_address,
    "state": chosen_state,
    "city": chosen_city
}
        return expected



    def upload_file(self):
        file_name, path = file_generated()
        self.element_is_present(self.locators.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        return file_name
    

    def random_subject(self):
                
        k = random.randint(1, len(SUBJECTS_LIST))

        chosen_lables = random.sample(SUBJECTS_LIST, k)

        for i in chosen_lables:
            element = self.element_is_visible(self.locators.SUBJECTS)
            
            element.send_keys(i)
            
            self.value_in_element_is_present(self.locators.SUBJECTS, value=i)
            
            element.send_keys(Keys.ENTER)

            self.value_in_element_is_present(self.locators.SUBJECTS, value="")

        return chosen_lables


    def random_state(self):

        state_id = self.element_is_clickable(self.locators.SELECTOR_STATE_ID)
        state_id.click()
        random_state = random.randint(1, 4)
        for _ in range(random_state):
            state_input = self.element_is_visible(self.locators.SELECTOR_STATE_INPUT)
            state_input.send_keys(Keys.ARROW_DOWN)
        state_input.send_keys(Keys.ENTER)
        chosen_state = self.elements_are_presents(self.locators.STATE_AND_CITY_TEXT)[0].text  #в return
        return chosen_state
    
    def random_city(self):

        city_id = self.element_is_clickable(self.locators.SELECTOR_CITY_ID)
        city_id.click()
        random_city = random.randint(1, 4)
        for _ in range(random_city):
            city_input = self.element_is_present(self.locators.SELECTOR_CITY_INPUT)
            city_input.send_keys(Keys.ARROW_DOWN)
        city_input.send_keys(Keys.ENTER)
        chosen_city = self.elements_are_presents(self.locators.STATE_AND_CITY_TEXT)[1].text  #в return
        return chosen_city
    

    def get_displayed_data(self):
        result = {}
        rows = self.elements_are_presents(self.locators.DISPLAYED_DATA)

        for row in rows:
            cells = row.find_elements("tag name", "td")
            if len(cells) == 2:
                label = cells[0].text.strip()
                value = cells[1].text.strip()
                result[label] = value

        return result
    
    def close_button_click(self):
        element = self.element_is_visible(self.locators.CLOSE_BUTTON)
        element.click()
        self.element_is_not_visible(self.locators.MODAL_CONTENT)
              




