from pages.windows_widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage
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

    class TestDatePickerPage:

        def test_select_date(self, driver):
            page = DatePickerPage(driver, url="https://demoqa.com/date-picker")
            page.open()
            displayed_date, day, month, year = page.select_date()
            assert f"{month:02d}/{int(day):02d}/{year}" == displayed_date, "Неверное отображение выбранной даты или формат даты был изменен"
            

        def test_select_date_and_time(self, driver):
            page = DatePickerPage(driver, url="https://demoqa.com/date-picker")
            page.open()
            expected_date, displayed_date  = page.select_data_and_time()
            assert displayed_date == expected_date, "Выбранные дата и время не совпадают с отображаемыми"

    class TestSliderPage:

        def test_slider(self, driver):
            page = SliderPage(driver, "https://demoqa.com/slider")
            page.open()
            value_before, value_after = page.move_slider()
            assert value_after != value_before, "Слайдер не двигается или значение не изменилось"

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            page.open()
            after, before = page.start_stop_progress_bar()
            assert after != before, f"Progress bar не изменился: начальное значение {before}, конечное {after}"

        def test_progress_bar_reset(self, driver):
            page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            page.open()
            after, before = page.reset_full_progress_bar()
            assert after == before, f"Progress bar не был сброшен: начальное значение {before}, конечное {after}"



            
            


            


            