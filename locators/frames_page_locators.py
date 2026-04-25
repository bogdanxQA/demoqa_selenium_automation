from selenium.webdriver.common.by import By


class FramesPageLocators:

    FIRST_FRAME = (By.CSS_SELECTOR, "#frame1")                  # //iframe[@id='frame1']
    SECOND_FRAME = (By.CSS_SELECTOR, "#frame2")                 # //iframe[@id='frame2']    
    FRAME_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")   # //h1[@id='sampleHeading']
