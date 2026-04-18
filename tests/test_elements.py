from pages.elements_page import TextBoxPage
import time


"""Просто чекнул что ворк НУЖНО УДАЛИТЬ"""
# def test_zhopa(driver):
#     page = BasePage(driver=driver, url="https://demoqa.com/")
#     page.open()
#     time.sleep(5)
""""""

def test_text_box(driver):
    page = TextBoxPage(driver=driver, url="https://demoqa.com/text-box")
    page.open()
    full_name, email, current_address, permanent_address = page.fill_all_inputs()
    created_full_name, created_email, created_current_address, created_permanent_address = page.check_created_form()
    assert full_name == created_full_name, f"Ожидаемый full_name: {full_name} не соответствует фактическому: {created_full_name}"
    assert email == created_email, f"Ожидаемый email: {email} не соответствует фактическому: {created_email}"
    assert current_address == created_current_address, f"Ожидаемый current_address: {current_address} не соответствует фактическому: {created_current_address}"
    assert permanent_address == created_permanent_address, f"Ожидаемый permanent_address: {permanent_address} не соответствует фактическому: {created_permanent_address}"
    
    
    
