from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, ModalDialogsPage, FramesPage, NestedFramesPage
import pytest






class TestAlertsFrameWindows:

    class TestBrowserWindows:

        def test_new_tab_button(self, driver):
            page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            page.open()
            page.click_to_new_tab_button()
            page.switch_to_new_tab()
            displayed_text = page.get_text_from_sample_page()
            assert "This is a sample page" == displayed_text, "Новая вкладка не была открыта, либо открыта не верная вкладка"


        def test_new_window_button(self, driver):
            page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            page.open()
            page.click_to_new_window_button()
            page.switch_to_new_tab()
            displayed_text = page.get_text_from_sample_page()
            assert "This is a sample page" == displayed_text, "Новое окно не было открыто, либо открыто не верное окно"


    class TestAlerts:

        def test_alert_button(self, driver):
            page = AlertsPage(driver, "https://demoqa.com/alerts")
            page.open()
            page.click_to_alert_button()
            page.accept_alert()
            assert page.is_alert_closed(), "Alert не был закрыт после его принятия"

        def test_alert_after_time_button(self, driver):
            page = AlertsPage(driver, "https://demoqa.com/alerts")
            page.open()
            page.click_to_alert_after_time_button()
            page.accept_alert()
            assert page.is_alert_closed(), "Alert не был закрыт после его принятия"

        
        @pytest.mark.parametrize("action, expected", [
            ("accept", "You selected Ok"),
            ("dismiss", "You selected Cancel")
        ])
        def test_confirm_box_button(self, driver, action, expected):
            page = AlertsPage(driver, "https://demoqa.com/alerts")
            page.open()
            page.click_to_confirm_box_button()
            if action == "accept":
                page.accept_alert()
                
            else:
                page.dismiss_alert()

            result = page.get_result_from_confirm_box()
            assert page.is_alert_closed(), "Alert не был закрыт после его принятия или отклонения"
            assert result == expected, f"После нажатия на {action} ожидался текст: {expected}.\n Полученный текст: {result}"


        def test_prompt_box_button(self, driver):
            page = AlertsPage(driver, "https://demoqa.com/alerts")
            page.open()
            page.click_to_prompt_box_button()
            expected_value = page.input_random_text_into_alert()
            page.accept_alert()
            displayed_value = page.get_result_from_prompt_box()
            assert page.is_alert_closed(), "Alert не был закрыт после его принятия"
            assert expected_value in displayed_value, f"Введенный текст в алерт: {expected_value} не найдет в отображаемом результате: {displayed_value}"


    class TestModalDialogs:

        def test_small_modal(self, driver):
            page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            page.open()
            page.click_to_small_modal_button()
            page.click_to_close_small_modal()
            assert page.is_modal_closed() == True, "Не удалось закрыть модальное окно"


        def test_large_modal(self, driver):
            page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            page.open()
            page.click_to_large_modal_button()
            page.click_to_close_large_modal()
            assert page.is_modal_closed() == True, "Не удалось закрыть модальное окно"

    class TestFrames:

        def test_first_frame(self,driver):
            page = FramesPage(driver, "https://demoqa.com/frames")
            page.open()
            result = page.get_data_from_first_frame()
            excepted = ['This is a sample page', "500px", "350px"]
            print(result)
            assert excepted == result, "Фрейм не существует или был изменен"

        def test_second_frame(self,driver):
            page = FramesPage(driver, "https://demoqa.com/frames")
            page.open()
            result = page.get_data_from_second_frame()
            excepted = ['This is a sample page', "100px", "100px"]
            print(result)
            assert excepted == result, "Фрейм не существует или был изменен"

    class TestNestedFrames:

        def test_parent_frame(self, driver):
            page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            page.open()
            result = page.switch_to_parent_frame()
            assert result == "Parent frame", "Фрейм не существует или был изменен"
            

        def test_child_frame(self, driver):
            page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            page.open()
            page.switch_to_parent_frame()
            result = page.switch_to_child_frame()
            assert result == "Child Iframe", "Фрейм не существует или был изменен"
            
            
        
            



            


        
            

