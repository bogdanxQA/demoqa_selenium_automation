from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage
import pytest



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

    class TestResizablePage:

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


    class TestDroppablePage:

        def test_simple_tab_drag_and_drop(self, driver):
            page = DroppablePage(driver, "https://demoqa.com/droppable")
            page.open()
            result, hex_color = page.drag_and_drop_simple()
            assert result == "Dropped!", "Элемент не был перемещен или изменился текст в drop box после перемещения"
            assert hex_color == "#4682b4", "Цвет элемента после перемещения не изменился"

        def test_acceptable_in_acept_tab_drag_and_drop(self, driver):
            page = DroppablePage(driver, "https://demoqa.com/droppable")
            page.open()
            hex_color_before, hex_color_after_click_and_hold, hex_color_after_drop, res = page.drag_and_drop_acceptable()
            assert hex_color_before == "#000000", "Изначальный цвет элемента Drop-container изменился. Ожидался #000000"
            assert hex_color_after_click_and_hold == "#3cb371", "Цвет Drop-container после захвата droppable элемента изменился. Ожидался #3cb371"
            assert hex_color_after_drop == "#4682b4", "Цвет Drop-container после перемещения в него droppable элемента изменился. Ожидался #4682b4 "
            assert res == "Dropped!", "Элемент не был перемещен или изменился текст в drop box после перемещения"

        def test_not_acceptable_in_acept_tab_drag_and_drop(self, driver):
            page = DroppablePage(driver, "https://demoqa.com/droppable")
            page.open()
            res = page.drag_and_drop_not_acceptable()
            assert res == "Drop here", "Элемент Drop-container неверно отреагировал на перемещение в него Not Acceptable droppable элемента"

        
        def test_not_greedy_outer_drag_and_drop(self, driver):
            page = DroppablePage(driver, "https://demoqa.com/droppable")
            page.open()
            hex_color_before, hex_color_after_click_and_hold, hex_color_after_drop, res = page.drag_and_drop_not_greedy_box("outer")
            assert hex_color_before == "#000000", "Изначальный цвет элемента Drop-container изменился. Ожидался #000000"
            assert hex_color_after_click_and_hold == "#3cb371", "Цвет Drop-container после захвата droppable элемента изменился. Ожидался #3cb371"
            assert hex_color_after_drop == "#4682b4", "Цвет Drop-container после перемещения в него droppable элемента изменился. Ожидался #4682b4 "
            assert res[0] == "Dropped!", "Элемент не был перемещен. Или текст отображаемый после перемещения был изменен"
            assert res[1] == "Inner droppable (not greedy)", "Изменилось расположение inner drop box или текст отображаемый при непопадании элемента в drop box был изменен."

        def test_not_greedy_inner_drag_and_drop(self, driver):
            page = DroppablePage(driver, "https://demoqa.com/droppable")
            page.open()
            hex_color_before, hex_color_after_click_and_hold, hex_color_after_drop, res = page.drag_and_drop_not_greedy_box("inner")
            assert hex_color_before == "#000000", "Изначальный цвет элемента Drop-container изменился. Ожидался #000000"
            assert hex_color_after_click_and_hold == "#3cb371", "Цвет Drop-container после захвата droppable элемента изменился. Ожидался #3cb371"
            assert hex_color_after_drop == "#4682b4", "Цвет Drop-container после перемещения в него droppable элемента изменился. Ожидался #4682b4 "
            assert res[0] == "Dropped!" and res[1] == "Dropped!" , "Элемент не был перемещен. Или текст отображаемый после перемещения был изменен"

        def test_greedy_outer_drag_and_drop(self, driver):
            page = DroppablePage(driver, "https://demoqa.com/droppable")
            page.open()
            hex_color_before, hex_color_after_click_and_hold, hex_color_after_drop, res = page.drag_and_drop_greedy_box("outer")
            assert hex_color_before == "#000000", "Изначальный цвет элемента Drop-container изменился. Ожидался #000000"
            assert hex_color_after_click_and_hold == "#3cb371", "Цвет Drop-container после захвата droppable элемента изменился. Ожидался #3cb371"
            assert hex_color_after_drop == "#4682b4", "Цвет Drop-container после перемещения в него droppable элемента изменился. Ожидался #4682b4 "
            assert res[0] == "Dropped!", "Элемент не был перемещен. Или текст отображаемый после перемещения был изменен"
            assert res[1] == "Inner droppable (greedy)", "Изменилось расположение inner drop box или текст отображаемый при непопадании элемента в drop box был изменен."

        def test_greedy_inner_drag_and_drop(self, driver):
            page = DroppablePage(driver, "https://demoqa.com/droppable")
            page.open()
            hex_color_before, hex_color_after_click_and_hold, hex_color_outer_after_drop, hex_color_inner_after_drop, res = page.drag_and_drop_greedy_box("inner")
            assert hex_color_before == "#000000", "Изначальный цвет элемента Drop-container изменился. Ожидался #000000"
            assert hex_color_after_click_and_hold == "#3cb371", "Цвет Drop-container после захвата droppable элемента изменился. Ожидался #3cb371"
            assert hex_color_outer_after_drop == "#000000", "Цвет outer drop box после перемещения в него droppable элемента изменился. Ожидался #000000 "
            assert hex_color_inner_after_drop == "#4682b4", "Цвет inner drop box после перемещения в него droppable элемента изменился. Ожидался #4682b4 "
            assert res[0] == "Outer droppable" and res[1] == "Dropped!" , "Элемент не был перемещен. Или текст отображаемый после перемещения был изменен"

        def test_revertable_item(self, driver):
            page = DroppablePage(driver, "https://demoqa.com/droppable")
            page.open()
            left, top, res = page.drag_and_drop_revert_and_not_revert_item("revert")
            assert (left, top) == ("0px", "0px"), "Revertable элемент не вернулся на изначальную позицию после drag and drop."
            assert res == "Dropped!", "Элемент не был перемещен или изменился текст в drop box после перемещения"

        def test_not_revertable_item(self, driver):
            page = DroppablePage(driver, "https://demoqa.com/droppable")
            page.open()
            left, top, res = page.drag_and_drop_revert_and_not_revert_item("not_revert")
            assert (left, top) != ("0px", "0px"), "Not revertable элемент изменил свою позицию после drag and drop."
            assert res == "Dropped!", "Элемент не был перемещен или изменился текст в drop box после перемещения"

    
    class TestDragabblePage:

        def test_simple_drag_box_move(self, driver):
            page = DragabblePage(driver, "https://demoqa.com/dragabble")
            page.open()
            position_after, position_before = page.simple_drag_box()
            assert position_after != position_before, f"Элемент drag_box не был перемещен"


        def test_only_x_drag_box_move(self, driver):
            page = DragabblePage(driver, "https://demoqa.com/dragabble")
            page.open()
            position_after, position_before = page.axis_restricted_drag_box("only_x")
            assert position_after["y"] == position_before["y"] and position_after["x"] != position_before["x"], \
            f"Элемент должен смещаться только по горизонтали. " \
            f"Позиция до: ({position_before}), после: ({position_after}). " \
            f"Ошибка: {'Y изменился' if position_after['y'] != position_before['y'] else 'X не изменился'}"

        def test_only_y_drag_box_move(self, driver):
            page = DragabblePage(driver, "https://demoqa.com/dragabble")
            page.open()
            position_after, position_before = page.axis_restricted_drag_box("only_y")
            assert position_after["x"] == position_before["x"] and position_after["y"] != position_before["y"], \
            f"Элемент должен смещаться только по вертикали. " \
            f"Позиция до: ({position_before}), после: ({position_after}). " \
            f"Ошибка: {'X изменился' if position_after['x'] != position_before['x'] else 'Y не изменился'}"


        def test_container_restricted_drag_and_drop(self, driver):
            page = DragabblePage(driver, "https://demoqa.com/dragabble")
            page.open()
            data = page.drag_and_drop_with_bounds()
            start, end = data['start'], data['end']
            left, top, right, bottom = data['bounds']
            width, height = data['size']['width'], data['size']['height']
            
            assert start != end, "Элемент не сдвинулся"
            assert end['x'] >= left and end['x'] + width <= right, "Элемент вышел за горизонтальные границы"
            assert end['y'] >= top and end['y'] + height <= bottom, "Элемент вышел за вертикальные границы"

            


            
            
           
            





