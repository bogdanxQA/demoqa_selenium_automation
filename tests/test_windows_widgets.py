from pages.windows_widgets_page import AccordianPage
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
            