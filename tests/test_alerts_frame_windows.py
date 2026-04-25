from pages.alerts_frame_windows_page import BrowserWindowsPage




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


        
            

