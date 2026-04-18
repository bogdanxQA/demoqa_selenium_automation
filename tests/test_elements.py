from pages.elements_page import TextBoxPage, CheckBoxPage
import time


"""Просто чекнул что ворк НУЖНО УДАЛИТЬ"""
# def test_zhopa(driver):
#     page = BasePage(driver=driver, url="https://demoqa.com/")
#     page.open()
#     time.sleep(5)
""""""


class TestElements:
    class TestTextBoxPage:
        def test_text_box(self, driver):
            page = TextBoxPage(driver=driver, url="https://demoqa.com/text-box")
            page.open()
            full_name, email, current_address, permanent_address = page.fill_all_inputs()
            created_full_name, created_email, created_current_address, created_permanent_address = page.check_created_form()
            assert full_name == created_full_name, f"Ожидаемый full_name: {full_name} не соответствует фактическому: {created_full_name}"
            assert email == created_email, f"Ожидаемый email: {email} не соответствует фактическому: {created_email}"
            assert current_address == created_current_address, f"Ожидаемый current_address: {current_address} не соответствует фактическому: {created_current_address}"
            assert permanent_address == created_permanent_address, f"Ожидаемый permanent_address: {permanent_address} не соответствует фактическому: {created_permanent_address}"
    
    
    class TestCheckBoxPage:
        def test_check_box(self, driver):
            page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            page.open()
            page.open_full_list()
            page.random_click_to_checkbox()
            expected_res = page.get_selected_checkbox_labels()
            displayed_res = page.get_displayed_selected_values() 
            assert set(displayed_res) == set(expected_res), f"Ожидаемый результат: {expected_res} не совпадает с фактическим: {displayed_res}"
            
            
            
    
