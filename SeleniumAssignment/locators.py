from selenium.webdriver.common.by import By

class FormLocators:
    EMAIL = (By.XPATH, "//input[@id='shub99']")
    PASSWORD = (By.XPATH, "//input[@id='pass']")
    COMPANY = (By.XPATH, "//input[@placeholder='Enter your company']")
    PHONE = (By.XPATH, "//input[@placeholder='Enter your mobile number']")
    SUBMIT = (By.XPATH, "//button[normalize-space()='Submit']")
    NEXT_BTN = (By.XPATH, "//button[normalize-space()='Next']")
    SELECT_ALL = (By.XPATH, "//input[@id='ohrmList_chkSelectAll']")
    NAME_TOGGLE = (By.XPATH, "//label[normalize-space()='Can you enter name here through automation']//*[name()='svg']")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Enter name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Enter Last name']")
    DATE_INPUT = (By.CSS_SELECTOR, "input[name='the_date']")
    DROPDOWN = (By.XPATH, "//select[@id='cars']")
    FILE_UPLOAD = (By.CSS_SELECTOR, "input[type='file']")
    MODAL_OPEN = (By.XPATH, "//button[normalize-space()='Open Modal']")
    MODAL_CLOSE = (By.XPATH, "//span[@class='close']")
    CONFIRM_BTN = (By.XPATH, "//button[normalize-space()='Show Confirmation']")
    PROMPT_BTN = (By.XPATH, "//button[normalize-space()='Show Prompt']")
    OPEN_XPATH_PAGE = (By.XPATH, "//button[normalize-space()='Open XPath Practice Page']")
    DOWNLOAD_FILE = (By.XPATH, "//button[normalize-space()='Download File']")
    XPATH_INPUT = (By.XPATH, "//input[@placeholder='Enter XPath or CSS Selector']")
    TEST_BTN = (By.XPATH, "//button[normalize-space()='Test']")
    SHADOW_HOST = ".shadow-container"
    IFRAME_INPUT = (By.CSS_SELECTOR, "input")
    IFRAME_BUTTON = (By.ID, "testButton")
