from pages.windows_widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, ToolTipsPage, MenuPage, SelectMenuPage
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

    class TestTabsPage:

        def test_what_tab(self, driver):
            page = TabsPage(driver, "https://demoqa.com/tabs")
            page.open()
            content, is_opend = page.open_what_tab_and_get_content()
            assert is_opend == "true", "Нажатие на tab с именем What не привело к раскрытию контента"
            assert len(content)>0, "Контент в tab = What отсутствует"

        def test_origin_tab(self, driver):
            page = TabsPage(driver, "https://demoqa.com/tabs")
            page.open()
            content, is_opend = page.open_origin_tab_and_get_content()
            assert is_opend == "true", "Нажатие на tab с именем Origin не привело к раскрытию контента"
            assert len(content)>0, "Контент в tab = Origin отсутствует"

        def test_use_tab(self, driver):
            page = TabsPage(driver, "https://demoqa.com/tabs")
            page.open()
            content, is_opend = page.open_use_tab_and_get_content()
            assert is_opend == "true", "Нажатие на tab с именем Use не привело к раскрытию контента"
            assert len(content)>0, "Контент в tab = Use отсутствует"

        @pytest.mark.xfail(reason="Кнопка всегда неактивна. Known Bug")
        def test_more_tab(self, driver):
            page = TabsPage(driver, "https://demoqa.com/tabs")
            page.open()
            content, is_opend = page.open_use_tab_and_get_content()
            assert is_opend == "true", "Нажатие на tab с именем More не привело к раскрытию контента"
            assert len(content)>0, "Контент в tab = More отсутствует"

    class TestToolTipsPage:

        def test_hover_me_button(self, driver):
            page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            page.open()
            content = page.hover_to_button_and_get_content()
            assert content == "You hovered over the Button", "Hover отсутствует или изменился контет"

        def test_hover_me_input(self, driver):
            page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            page.open()
            content = page.hover_to_input_and_get_content()
            assert content == "You hovered over the text field", "Hover отсутствует или изменился контет"

        def test_hover_to_contrary(self, driver):
            page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            page.open()
            content = page.hover_to_contrary_and_get_content()
            assert content == "You hovered over the Contrary", "Hover отсутствует или изменился контет"

        def test_hover_to_text(self, driver):
            page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            page.open()
            content = page.hover_to_text_and_get_content()
            assert content == "You hovered over the 1.10.32", "Hover отсутствует или изменился контет"

    class TestMenuPage:

        def test_check_menu_items(self, driver):
            page = MenuPage(driver, "https://demoqa.com/menu")
            page.open()
            data = page.check_menu()
            assert ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'] == data, "Раскрываются не все элементы меню"


    class TestSelectMenuPage:

        def test_random_select_value(self, driver):
            page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            page.open()
            chosen_option, displayed_text = page.select_random_value_in_first_selector()
            assert chosen_option == displayed_text, f"В списке выбора отсутствует опция {chosen_option} или после ее выбора данные отобразились некорректно"

        def test_random_select_one(self, driver):
            page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            page.open()
            chosen_option, displayed_text = page.select_random_value_in_second_selector()
            assert chosen_option == displayed_text, f"В списке выбора отсутствует опция {chosen_option} или после ее выбора данные отобразились некорректно"

        def test_old_style_select_menu(self, driver):
            page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            page.open()
            chosen_color, selected_value = page.select_random_color_in_old_style_select_menu()
            assert chosen_color == selected_value, "Выбранный цвет отличается от отображаемого"

        def test_random_multi_select_drop_down(self, driver):
            page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            page.open()
            chosen_colors = page.multi_select_drop_down()
            displayed_colors = page.get_displayed_colors_in_multi_select()
            assert chosen_colors == displayed_colors, "Не все выбранные значения отобразились в интерфейсе"

        

            
            


            
            
