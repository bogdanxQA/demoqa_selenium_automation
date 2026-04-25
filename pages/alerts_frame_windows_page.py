from pages.base_page import BasePage
from locators.browser_windows_page_locators import BrowserWindowsPageLocators


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

    

    
        

