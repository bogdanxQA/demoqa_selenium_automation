from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage
import time



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

    class TestRadioButtonPage:
        def test_radio_button_yes(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_to_radio_button_yes()
            assert "Yes" in radio_button_page.get_displayed_selected_button(), "Yes не отображается в выбранных"

        def test_radio_button_impressive(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_to_radio_button_impressive()
            assert "Impressive" in radio_button_page.get_displayed_selected_button(), "Impressive не отображается в выбранных"

        def test_radio_button_no(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_to_radio_button_no()
            assert "No" in radio_button_page.get_displayed_selected_button(), "No не отображается в выбранных"

    class TestWebTablesPage:
        def test_add_new_data(self, driver):
            web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables_page.open()
            excepted_data = web_tables_page.add_new_data(count=1)
            full_data = web_tables_page.get_full_data()
            
            for record in excepted_data:
             assert record in full_data, f"Запись '{record}' не найдена в таблице"


        def test_search_and_result(self, driver):
            page = WebTablesPage(driver, "https://demoqa.com/webtables")
            page.open()
            name = page.add_new_data()[0].split()[0] 
            excepted_data = page.search_box_clear_and_send_keys(send_keys=name)
            displayed_data = page.get_full_data()
            assert excepted_data in displayed_data[0], f"Ожидаемого значения {excepted_data} не обнаружено в отображенном результате {displayed_data[0]}"

        
        def test_update_data(self, driver):
            page = WebTablesPage(driver, "https://demoqa.com/webtables")
            page.open()
            name = page.add_new_data()[0].split()[0] 
            page.search_box_clear_and_send_keys(send_keys=name)
            excepted_data = page.update_data()
            displayed_data = page.get_full_data()[0]
                        
            for field, expected_value in excepted_data.items():
                assert expected_value in displayed_data, f"Поле '{field}' со значением '{expected_value}' не обнаружено в отображенном результате: {displayed_data}"


        def test_delete_data(self, driver):
            page = WebTablesPage(driver, "https://demoqa.com/webtables")
            page.open()
            name = page.add_new_data()[0].split()[0] 
            page.search_box_clear_and_send_keys(send_keys=name)
            page.delete_data()
            displayed_data = page.get_full_data_wo_wait()
            assert displayed_data == [], f"После удаления данные остались в таблице: {displayed_data}"


        
        """Проверяем на максимальном селекте сколько отображается строк. Добиваем до 50-ти проверяем каждый селект (сколько отображает)"""        
        def test_show_button(self,driver):
            page = WebTablesPage(driver, "https://demoqa.com/webtables")
            page.open()
            page.select_show_value()
            total_records = len(page.get_full_data())
            if total_records < 50:
                need = 50 - total_records
                page.add_new_data(count=need)
                total_records = len(page.get_full_data())

            for value in [10, 20, 30, 40 ,50]:
                page.select_show_value(value)
                visible = len(page.get_full_data())
                assert value == visible, f"При выборе 'Show {value}' ожидалось {value} строк, получено {visible}"


        #def можно добавить проверку пагинации, но необходимо много тестовых данных
            

            
                    

        

            
            
            
            
    
