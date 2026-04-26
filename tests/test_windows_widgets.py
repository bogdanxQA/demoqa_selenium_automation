from pages.windows_widgets_page import AccordianPage, AutoCompletePage
import pytest

class TestWindowsWidgets:

    class TestAccordianPage:

        
        @pytest.mark.parametrize("button_number, expected_title", [
            (0, "What is Lorem Ipsum?"),
            (1, "Where does it come from?"),
            (2, "Why do we use it?")
        ])
        def test_accordian_button(self, driver, button_number, expected_title):
            page = AccordianPage(driver, url="https://demoqa.com/accordian")
            page.open()
            title, content, is_opened = page.open_get_and_close_content_from_accordian(button_number)
            assert title == expected_title
            assert len(content) > 0
            assert is_opened == 'false'


    class TestAutoCompletePage:

        def test_multiple_input(self,driver):
            page = AutoCompletePage(driver, url="https://demoqa.com/auto-complete")
            page.open()
            expected_value = page.random_fill_multiple_input()
            displayed_value = page.get_data_from_multiple_input()
            assert sorted(expected_value) == sorted(displayed_value), f"Расхождение в цветах.\nЛишние: {set(displayed_value) - set(expected_value)}\nНе хватает: {set(expected_value) - set(displayed_value)}"

        def test_single_input(self, driver):
            page = AutoCompletePage(driver, url="https://demoqa.com/auto-complete")
            page.open()
            expected_value = page.random_fill_single_input()
            displayed_value = page.get_data_from_single_input()
            assert expected_value == displayed_value

            


            