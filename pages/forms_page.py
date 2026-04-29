from pages.base_page import BasePage
from locators.practice_form_page_locators import PracticeFormPageLocators
from data.generator.generator import practice_form_data_generated, file_generated
from data.data import SUBJECTS_LIST
from selenium.webdriver.common.keys import Keys
import random
import os
import allure


class PracticeFormPage(BasePage):

    locators = PracticeFormPageLocators()

    @allure.step("Fill all fields with random data")
    def fill_all_inputs(self):
         
        students_form = next(practice_form_data_generated())

        first_name = students_form.first_name 
        last_name = students_form.last_name 
        email = students_form.email 
        mobile_number = students_form.mobile_number 
        current_address = students_form.current_address 

        with allure.step("Fill name, email, mobile number, address"):
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(mobile_number)
            self.element_is_visible(self.locators.CURRENT_ADRESS).send_keys(current_address)

        """Выбор рандомной радиокнопки + return value. Другой способ в локаторах"""
        with allure.step("Select random gender"):
            gender_locators = [
                self.locators.MALE_RADIO_BUTTON,
                self.locators.FEMALE_RADIO_BUTTON,
                self.locators.OTHER_RADIO_BUTTON
            ]
            chosen_random_gender_locator = random.choice(gender_locators)
            random_gender_element = self.element_is_visible(chosen_random_gender_locator)
            chosen_gender_value = random_gender_element.get_attribute("value")   
            random_gender_element.click()
     
        """Выбор рандомных чекбоксов + return label"""
        with allure.step("Select random hobbies"):
            check_box_locators = [
                (self.locators.SPORTS_CHECKBOX, "Sports"),
                (self.locators.MUSIC_CHECKBOX, "Music"),
                (self.locators.READING_CHECKBOX, "Reading")
            ]
            k = random.randint(1, len(check_box_locators))
            chosen_locators = random.sample(check_box_locators, k)
            selected_checkbox_values = []  
            for locator, label in chosen_locators:
                self.element_is_visible(locator).click()
                selected_checkbox_values.append(label)

        file_name = self.upload_file()   
        chosen_subjects = self.random_subject() 
        chosen_state = self.random_state() 
        chosen_city = self.random_city() 

        with allure.step("Submit form"):
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


    @allure.step("Updload generated file")
    def upload_file(self):
        file_name, path = file_generated()
        self.element_is_present(self.locators.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        return file_name
    
    @allure.step("Select random subjects")
    def random_subject(self):
        k = random.randint(1, len(SUBJECTS_LIST))
        chosen_lables = random.sample(SUBJECTS_LIST, k)

        for i in chosen_lables:
            with allure.step(f"Select subject: {i}"):
                element = self.element_is_visible(self.locators.SUBJECTS)
                element.send_keys(i)
                self.value_in_element_is_present(self.locators.SUBJECTS, value=i)
                self.element_is_present(self.locators.SUBJECTS_AUTO_COMPLETE)
                element.send_keys(Keys.ENTER)
                self.value_in_element_is_present(self.locators.SUBJECTS, value="")

        return chosen_lables

    @allure.step("Select random state")
    def random_state(self):
        with allure.step("Open city dropdown"):
            state_id = self.element_is_clickable(self.locators.SELECTOR_STATE_ID)
            state_id.click()
        with allure.step("Navigate to random state using arrow keys"):
            random_state = random.randint(1, 4)
            state_input = self.element_is_visible(self.locators.SELECTOR_STATE_INPUT)
            for _ in range(random_state):
                state_input.send_keys(Keys.ARROW_DOWN)
            state_input.send_keys(Keys.ENTER)
        chosen_state = self.elements_are_presents(self.locators.STATE_AND_CITY_TEXT)[0].text  
        return chosen_state

    @allure.step("Select random city") 
    def random_city(self):
        with allure.step("Open city dropdown"):
            city_id = self.element_is_clickable(self.locators.SELECTOR_CITY_ID)
            city_id.click()
        with allure.step("Navigate to random city using arrow keys"):
            random_city = random.randint(1, 4)
            city_input = self.element_is_present(self.locators.SELECTOR_CITY_INPUT)
            for _ in range(random_city):
                city_input.send_keys(Keys.ARROW_DOWN)
            city_input.send_keys(Keys.ENTER)
        chosen_city = self.elements_are_presents(self.locators.STATE_AND_CITY_TEXT)[1].text  
        return chosen_city
    
    @allure.step("Get displayed data from result modal")
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
    
    @allure.step("Click close button")
    def close_button_click(self):
        element = self.element_is_visible(self.locators.CLOSE_BUTTON)
        element.click()
        self.element_is_not_visible(self.locators.MODAL_CONTENT)
