# test_main.py

import time
import pytest
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import methods
import testdata
import locators

# ========== PYTEST FIXTURE ==========

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    time.sleep(3)
    driver.quit()

# ========== TASK WRAPPERS FOR PARALLEL EXEC ==========

def run_with_fixture(test_func):
    """Simulate running pytest function manually with the 'driver' fixture"""
    # Setup driver like pytest fixture would
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    try:
        test_func(driver)
    except Exception as e:
        print(f"❌ Error in {test_func.__name__}: {e}")
    finally:
        time.sleep(3)
        driver.quit()

# ========== TEST FUNCTIONS (USE FIXTURE STYLE) ==========

def test_task1(driver):
    methods.open_homepage(driver, testdata.url)
    methods.verify_page_title(driver, "Amazon.in")
    methods.verify_element_visibility(driver, locators.search_box)
    methods.verify_element_visibility(driver, locators.sign_in_button)
    print("✅ Task 1 Completed")

def test_task2(driver):
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["wireless_mouse"])
    methods.verify_minimum_results(driver, 10)
    print("✅ Task 2 Completed")

def test_task3(driver):
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["headphones"])
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)
    methods.apply_price_filter(driver)
    methods.verify_minimum_results(driver, 1)
    print("✅ Task 3 Completed")

def test_task4(driver):
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["power_bank"])
    time.sleep(5)
    methods.sort_by_low_to_high(driver)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    time.sleep(3)
    methods.verify_price_order(driver)
    print("✅ Task 4 Completed")

def test_task5(driver):
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["keyboard"])
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(2)
    methods.add_product_to_cart(driver, locators.first_product_xpath, locators.add_to_cart_xpath)
    print("✅ Task 5 Completed")

def test_task6(driver):
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["keyboard"])
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(2)
    methods.add_product_to_cart(driver, locators.first_product_xpath, locators.add_to_cart_xpath)
    methods.proceed_to_checkout_without_login(driver)
    print("✅ Task 6 Completed")

def test_task7(driver):
    methods.open_homepage(driver, testdata.url)
    methods.invalid_search_check(driver, locators.search_box, testdata.search_terms["invalid"])
    print("✅ Task 7 Completed")

def test_task8(driver):
    methods.open_homepage(driver, testdata.url)
    time.sleep(2)
    methods.click_mobiles_link(driver, locators.mobiles_link)
    print("✅ Task 8 Completed")

def test_task9(driver):
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["mobile"])
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(2)
    methods.add_to_wishlist_without_login(driver, locators.sponsored_product_xpath, locators.wishlist_button_xpath)
    print("✅ Task 9 Completed")

# ========== MANUAL PARALLEL RUNNER ==========

# Wrap test functions for parallel execution
tasks = [
    test_task1, test_task2, test_task3, test_task4, test_task5,
    test_task6, test_task7, test_task8, test_task9
]

if __name__ == "__main__":
    print("🚀 Starting parallel tests with pytest fixture emulation...\n")

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(run_with_fixture, tasks)

    print("\n🎉 All tasks completed.")
