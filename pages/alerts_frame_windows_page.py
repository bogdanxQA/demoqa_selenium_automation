from pages.base_page import BasePage
from locators.browser_windows_page_locators import BrowserWindowsPageLocators
from locators.alerts_page_locators import AlertsPageLocators
from locators.modal_dialogs_page_locators import ModalDialogsPageLocators
from locators.frames_page_locators import FramesPageLocators
from locators.nested_frames_page_locators import NestedFramesPageLocators
from data.generator.generator import data_genarated


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def click_to_new_tab_button(self):
        element = self.element_is_visible(self.locators.NEW_TAB_BUTTON)
        element.click()  
    
    def switch_to_new_tab(self):
        self.tab_or_window_is_opened(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def get_text_from_sample_page(self):
        element = self.element_is_present(self.locators.SAMPLE_PAGE_TEXT)
        return element.text
    
        
    def click_to_new_window_button(self):
        element = self.element_is_visible(self.locators.NEW_WINDOW_BUTTON)
        element.click()


class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    def click_to_alert_button(self):
        element = self.element_is_visible(self.locators.ALERT_BUTTON)
        element.click()

    def click_to_alert_after_time_button(self):
        element = self.element_is_visible(self.locators.ALERT_AFTER_TIME_BUTTON)
        element.click()

    def click_to_confirm_box_button(self):
        element = self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON)
        element.click()

    def click_to_prompt_box_button(self):
        element = self.element_is_visible(self.locators.PROMPT_BOX_BUTTON)
        element.click()

    def accept_alert(self):
        alert = self.wait_for_alert()
        alert.accept()

    def dismiss_alert(self):
        alert = self.wait_for_alert()
        alert.dismiss()

    def get_result_from_confirm_box(self):
        result = self.element_is_present(self.locators.RESULT_CONFIRM_BUTTON).text
        return result
    
    def input_random_text_into_alert(self):
        random_text = next(data_genarated())
        text = random_text.first_name
        self.wait_for_alert().send_keys(text)
        return text
    
    def get_result_from_prompt_box(self):
        result = self.element_is_present(self.locators.RESULT_PROMPT_BUTTON).text
        return result
    
class ModalDialogsPage(BasePage):

    locators = ModalDialogsPageLocators()

    def click_to_small_modal_button(self):
        element = self.element_is_visible(self.locators.SMALL_MODAL_BUTTON)
        element.click()

    def click_to_large_modal_button(self):
        element = self.element_is_visible(self.locators.LARGE_MODAL_BUTTON)
        element.click()
    
    def click_to_close_small_modal(self):
        element = self.element_is_present(self.locators.CLOSE_SMALL_MODAL_BUTTON)
        element.click()

    def click_to_close_large_modal(self):
        element = self.element_is_present(self.locators.CLOSE_LARGE_MODAL_BUTTON)
        element.click()

    def is_modal_closed(self):
        return self.wait_for_element_to_disappear(self.locators.MODAL)
    

class FramesPage(BasePage):

    locators = FramesPageLocators()

    def get_data_from_first_frame(self):
        element = self.element_is_present(self.locators.FIRST_FRAME)
        width = element.get_attribute("width")
        height = element.get_attribute("height")
        self.driver.switch_to.frame(element)
        text = self.element_is_present(self.locators.FRAME_TITLE).text
        return [text, width, height]
    
    def get_data_from_second_frame(self):
        element = self.element_is_present(self.locators.SECOND_FRAME)
        width = element.get_attribute("width")
        height = element.get_attribute("height")
        self.driver.switch_to.frame(element)
        text = self.element_is_present(self.locators.FRAME_TITLE).text
        return [text, width, height]
    

class NestedFramesPage(BasePage):

    locators = NestedFramesPageLocators()

    def switch_to_parent_frame(self):
        element = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(element)
        text = self.element_is_present(self.locators.FRAME_TEXT).text
        return text.strip()
    
    def switch_to_child_frame(self):
        element = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(element)
        text = self.element_is_present(self.locators.FRAME_TEXT).text
        return text.strip()

        

    





    

    
        

