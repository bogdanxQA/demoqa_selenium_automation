from selenium.webdriver.common.by import By


class CheckBoxPageLocators:                                                             #xpath:
    TREE_SWITCHER = (By.CSS_SELECTOR, ".rc-tree-switcher.rc-tree-switcher_close")       # //span[@class = 'rc-tree-switcher rc-tree-switcher_close']   нужно прокликать в цикле пока не закончится    
    CHECK_BOX = (By.CSS_SELECTOR, "[role='checkbox']")                                  # //span[@role='checkbox']

    text_success = (By.CSS_SELECTOR, ".text-success")                                   # //span[@class='text-success']
    aria_checked = (By.CSS_SELECTOR, "[aria-checked='true']")



                                                                        
