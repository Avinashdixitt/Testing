# test_main.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import methods
import testdata
import locators

# Setup
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

try:
    # Task 1: Verify Homepage Loads
    methods.open_homepage(driver, testdata.url)
    methods.verify_page_title(driver, "Amazon.in")
    methods.verify_element_visibility(driver, locators.search_box)
    methods.verify_element_visibility(driver, locators.sign_in_button)
    print("✅ Task 1 Completed")

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # Task 2: Search for a Product
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["wireless_mouse"])
    methods.verify_minimum_results(driver, 10)
    print("✅ Task 2 Completed")

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # Task 3: Apply Price Filter
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["headphones"])
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)
    methods.apply_price_filter(driver)
    methods.verify_minimum_results(driver, 1)

    print("✅ Task 3 Completed")

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # Task 4: Sort Results
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["power_bank"])
    time.sleep(5)
    methods.sort_by_low_to_high(driver)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    time.sleep(3)
    methods.verify_price_order(driver)
    print("✅ Task 4 Completed")

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # Task 5: Add Product to Cart
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["keyboard"])
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(2)
    methods.add_product_to_cart(driver, locators.first_product_xpath, locators.add_to_cart_xpath)
    print("✅ Task 5 Completed")

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # Task 6: Attempt Checkout Without Login
    methods.proceed_to_checkout_without_login(driver)
    print("✅ Task 6 Completed")

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # Task 7: Check Invalid Search
    methods.open_homepage(driver, testdata.url)
    methods.invalid_search_check(driver, locators.search_box, testdata.search_terms["invalid"])
    print("✅ Task 7 Completed")

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # Task 8: Verify Navigation Links
    methods.open_homepage(driver, testdata.url)

    time.sleep(2)
    methods.click_mobiles_link(driver, locators.mobiles_link)
    print("✅ Task 8 Completed")

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # Task 9: Wishlist Without Login
    methods.open_homepage(driver, testdata.url)
    methods.search_product(driver, locators.search_box, testdata.search_terms["mobile"])
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(2)
    methods.add_to_wishlist_without_login(driver, locators.sponsored_product_xpath, locators.wishlist_button_xpath)
    print("✅ Task 9 Completed")

finally:
    time.sleep(5)
    driver.quit()
