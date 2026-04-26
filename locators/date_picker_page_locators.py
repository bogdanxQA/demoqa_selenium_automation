from selenium.webdriver.common.by import By


class DatePickerPageLocators: 

    SELECT_DATE_INPUT = (By.CSS_SELECTOR, "#datePickerMonthYearInput")
    SELECT_DAY = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'react-datepicker__day--outside-month'))]")
    SELECT_MONTH = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    SELECT_YEAR = (By.CSS_SELECTOR, ".react-datepicker__year-select")


    SELECT_MONTH_DATE_TIME = (By.CSS_SELECTOR, "button[class= 'react-datepicker__month-read-view']")
    SELECT_DATE_TIME_INPUT = (By.CSS_SELECTOR, "#dateAndTimePickerInput")
    SELECT_YEAR_DATE_TIME = (By.CSS_SELECTOR, "button[class= 'react-datepicker__year-read-view']")
    YEAR_DROPDOWN = (By.CSS_SELECTOR, ".react-datepicker__year-option")
    MONTH_DROPDOWN = (By.CSS_SELECTOR, ".react-datepicker__month-option")
    SELECT_TIME = (By.CSS_SELECTOR, "li[class = 'react-datepicker__time-list-item '] ")
    
