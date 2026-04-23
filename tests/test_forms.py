from pages.forms_page import PracticeFormPage
import pytest

import time

class TestForms():
    class TestPracticeFormPage:

        def test_practice_form_page(self, driver):

            page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
            page.open()
            expected_values = page.fill_all_inputs()
            displayed_value = page.get_displayed_data()
            assert displayed_value["Student Name"] == f"{expected_values['first_name']} {expected_values['last_name']}"
            assert displayed_value["Student Email"] == expected_values["email"]
            assert displayed_value["Gender"] == expected_values["gender"]
            assert displayed_value["Mobile"] == expected_values["mobile"]
            # Hobbies и Subjects в таблице приходят строкой через запятую
            assert displayed_value["Hobbies"] == ", ".join(expected_values["hobbies"])
            assert displayed_value["Subjects"] == ", ".join(expected_values["subjects"])
            assert displayed_value["Picture"] == expected_values["file_name"]
            assert displayed_value["Address"] == expected_values["address"]
            assert displayed_value["State and City"] == f"{expected_values['state']} {expected_values['city']}"

        @pytest.mark.xfail(reason="Кнопка Close не закрывает модальное окно (known bug)")
        def test_modal_close_button_does_not_work(self, driver):

            page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
            page.open()
            page.fill_all_inputs()
            page.close_button_click()
            
            