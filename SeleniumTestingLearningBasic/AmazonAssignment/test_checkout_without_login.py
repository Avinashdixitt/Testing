# test_checkout_without_login.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout_without_login(driver):
    driver.get("https://www.amazon.in/gp/cart/view.html")
    time.sleep(2)

    try:
        proceed_btn = driver.find_element(By.NAME, "proceedToRetailCheckout")
        proceed_btn.click()
        time.sleep(2)
    except:
        pytest.fail("Proceed to Buy button not found or not clickable")

    try:
        assert "signin" in driver.current_url or driver.find_element(By.ID, "ap_email").is_displayed()
    except:
        pytest.fail("Login page not displayed after attempting to checkout without login")
