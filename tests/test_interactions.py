from pages.interactions_page import SortablePage, SelectablePage, ResizablePage



class TestInteractions():

    class TestSortablePage:

        def test_move_elements_in_list(self, driver):
            page = SortablePage(driver, "https://demoqa.com/sortable")
            page.open()
            item_list_before, item_list_after = page.move_random_elements_in_list()
            assert item_list_before != item_list_after, "Перемещение элементов в списке не работает"

        def test_move_elements_in_grid(self, driver):
            page = SortablePage(driver, "https://demoqa.com/sortable")
            page.open()
            item_list_before, item_list_after = page.move_random_elements_in_grid()
            assert item_list_before != item_list_after, "Перемещение элементов в списке не работает"

    class TestSelectablePage:

        def test_selectable_list(self, driver):
            page = SelectablePage(driver, "https://demoqa.com/selectable")
            page.open()
            selected_items = page.select_random_inactive_items_in_list()
            active_items = page.get_active_items_in_list()
            for item in selected_items:
                assert item in active_items, f"Элемент {item} после клика по нему не стал активным"

        def test_selectable_grid(self, driver):
            page = SelectablePage(driver, "https://demoqa.com/selectable")
            page.open()
            selected_items = page.select_random_inactive_items_in_grid()
            active_items = page.get_active_items_in_grid()
            for item in selected_items:
                assert item in active_items, f"Элемент {item} после клика по нему не стал активным"

    class TestResizable:

        def test_max_min_size_resizable_box_with_boundaries(self, driver):
            page = ResizablePage(driver, "https://demoqa.com/resizable")
            page.open()
            max_size, min_size = page.change_size_in_resizable_box_with_boundaries()
            assert max_size[0] == "500px", f"Максимальная ширина изменяемого окна изменилась: получено {max_size[0]}, ожидалось 500px"
            assert max_size[1] == "300px", f"Максимальная высота изменяемого окна изменилась: получено {max_size[1]}, ожидалось 300px"
            assert min_size[0] == "150px", f"Максимальная ширина изменяемого окна изменилась: получено {min_size[0]}, ожидалось 150px"
            assert min_size[1] == "150px", f"Максимальная высота изменяемого окна изменилась: получено {min_size[1]}, ожидалось 150px"

        def test_resizable_box_wo_boundaries(self, driver):
            page = ResizablePage(driver, "https://demoqa.com/resizable")
            page.open()
            start_size, increased_size, min_size = page.change_size_in_resizable_wo_boundaries()
            assert increased_size != start_size, "Размер изменяемого окна без ограничений не изменился"
            assert min_size[0] == "20px", f"Максимальная ширина изменяемого окна изменилась: получено {min_size[0]}, ожидалось 20px"
            assert min_size[1] == "20px", f"Максимальная высота изменяемого окна изменилась: получено {min_size[1]}, ожидалось 20px"

