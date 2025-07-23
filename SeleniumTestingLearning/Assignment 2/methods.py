#this is for methods

from locators import FormLocators as loc
from test_data import TestData as data

import time
from selenium.webdriver.support.select import Select


def loginpage(driver):
# 1. Login Page
    try:
        driver.find_element(*loc.EMAIL).send_keys(data.EMAIL)
        driver.find_element(*loc.PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*loc.COMPANY).send_keys(data.COMPANY)
        driver.find_element(*loc.PHONE).send_keys(data.PHONE)
        driver.find_element(*loc.SUBMIT).click()
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 1")
    except Exception as e:
        print("Fail 1:", e)

    time.sleep(2)
def tablepage(driver):
    # 2. Select All Checkbox
    try:
        driver.find_element(*loc.SELECT_ALL).click()
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 2")
    except Exception as e:
        print("Fail 2:", e)
    time.sleep(2)
def namepage(driver):
    try:
        driver.find_element(*loc.NAME_TOGGLE).click()
        driver.find_element(*loc.FIRST_NAME).send_keys(data.FIRST_NAME)
        driver.find_element(*loc.LAST_NAME).send_keys(data.LAST_NAME)
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 3")
    except Exception as e:
        print("Fail 3:", e)
    time.sleep(2)
def datepage(driver):
    try:
        driver.find_element(*loc.DATE_INPUT).send_keys(data.DATE)
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 4")
    except Exception as e:
        print("Fail 4:", e)

    time.sleep(2)
def dropdownpage(driver):
    try:
        Select(driver.find_element(*loc.DROPDOWN)).select_by_value(data.VALUE)
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 5")
    except Exception as e:
        print("Fail 5:", e)

    time.sleep(2)

def fileuploadpage(driver):
    try:
        driver.find_element(*loc.FILE_UPLOAD).send_keys(data.FILE_PATH)
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 6")
    except Exception as e:
        print("Fail 6:", e)
    time.sleep(2)
def modalpage(driver):
    try:
        driver.find_element(*loc.MODAL_OPEN).click()
        time.sleep(2)
        driver.find_element(*loc.MODAL_CLOSE).click()
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 7")
    except Exception as e:
        print("Fail 7:", e)
    time.sleep(2)
def alertpage(driver):
    try:
        driver.find_element(*loc.CONFIRM_BTN).click()
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1)
        alert.accept()
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 8")
    except Exception as e:
        print("Fail 8:", e)
    time.sleep(2)

def promptpage(driver):
    try:
        driver.find_element(*loc.PROMPT_BTN).click()
        alert = driver.switch_to.alert
        alert.send_keys(data.PROMPT_TEXT)
        alert.accept()
        alert.accept()
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 9")
    except Exception as e:
        print("Fail 9:", e)
    time.sleep(2)

def xpathpage(driver):
    try:
        driver.find_element(*loc.OPEN_XPATH_PAGE).click()
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        driver.switch_to.window(tabs[0])
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 10")
    except Exception as e:
        print("Fail 10:", e)
    time.sleep(2)

def downloadpage(driver):
    try:
        driver.find_element(*loc.DOWNLOAD_FILE).click()
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 11")
    except Exception as e:
        print("Fail 11:", e)

    time.sleep(2)

def selectorpage(driver):
    try:
        driver.find_element(*loc.XPATH_INPUT).click()
        driver.find_element(*loc.XPATH_INPUT).send_keys(data.XPATH_INPUT)
        driver.find_element(*loc.TEST_BTN).click()
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 12")
    except Exception as e:
        print("Fail 12:", e)

    time.sleep(2)
def shadowdompage(driver):

    # 13. Shadow DOM + iFrame
    try:
        shadow_host = driver.execute_script(f'return document.querySelector("{loc.SHADOW_HOST}")')
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        iframe = driver.execute_script('return arguments[0].querySelector("iframe")', shadow_root)
        driver.switch_to.frame(iframe)
        driver.find_element(*loc.IFRAME_INPUT).send_keys("Hello")
        driver.find_element(*loc.IFRAME_BUTTON).click()
        driver.switch_to.default_content()
        driver.find_element(*loc.NEXT_BTN).click()
        print("Pass 13")
    except Exception as e:
        print("Fail 13:", e)
    time.sleep(2)
