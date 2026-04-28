from pages.interactions_page import SortablePage, SelectablePage



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
