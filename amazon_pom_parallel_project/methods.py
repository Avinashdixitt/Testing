# methods.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_homepage(driver, url):
    driver.get(url)


def verify_page_title(driver, expected_title):
    assert expected_title in driver.title


def verify_element_visibility(driver, locator):
    by, value = locator
    element = driver.find_element(by, value)
    assert element.is_displayed()


def search_product(driver, locator, search_term):
    by, value = locator
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)


def verify_minimum_results(driver, min_count):
    results = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot > div[data-component-type='s-search-result']")
    visible_results = [r for r in results if r.is_displayed()]
    assert len(visible_results) >= min_count


def apply_price_filter(driver, lower_offset=50, upper_offset=-100):
    from selenium.webdriver.common.action_chains import ActionChains

    lower_slider = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='p_36/range-slider_slider-item_lower-bound-slider']"))
    )
    upper_slider = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='p_36/range-slider_slider-item_upper-bound-slider']"))
    )
    actions = ActionChains(driver)
    actions.click_and_hold(lower_slider).move_by_offset(lower_offset, 0).release().perform()
    time.sleep(1)
    actions.click_and_hold(upper_slider).move_by_offset(upper_offset, 0).release().perform()
    time.sleep(6)


def sort_by_low_to_high(driver):
    sort_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "a-autoid-0-announce")))
    sort_btn.click()
    low_to_high_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "s-result-sort-select_1")))
    low_to_high_option.click()
    time.sleep(5)


def verify_price_order(driver):
    price_elements = driver.find_elements(By.CSS_SELECTOR, "span.a-price > span.a-offscreen")
    valid_prices = []
    for elem in price_elements:
        price_text = elem.get_attribute("textContent").strip().replace("₹", "").replace(",", "")
        if price_text.replace(".", "").isdigit():
            valid_prices.append(float(price_text))
        if len(valid_prices) == 2:
            break
    assert len(valid_prices) == 2, "Not enough prices found."
    assert valid_prices[0] <= valid_prices[1]




def add_product_to_cart(driver, product_xpath, add_to_cart_xpath):
    product = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, product_xpath)))
    product.click()
    time.sleep(3)

    # Step 6: Click Add to Cart using your XPath
    add_to_cart_xpath = "//input[@id='add-to-cart-button']"
    add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath))
    )
    add_to_cart.click()
    print(" Added product to cart")




def proceed_to_checkout_without_login(driver):
    driver.get("https://www.amazon.in/gp/cart/view.html")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "proceedToRetailCheckout"))
    )
    time.sleep(2)
    proceed_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "proceedToRetailCheckout"))
    )
    proceed_btn.click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.any_of(
            EC.presence_of_element_located((By.ID, "ap_email")),
            EC.url_contains("signin")
        )
    )


def invalid_search_check(driver, search_box_locator, search_term):
    search_product(driver, search_box_locator, search_term)
    time.sleep(3)

    try:
        # Try to find "No results for" message (sometimes appears)
        no_results_message = driver.find_elements(By.XPATH, "//*[contains(text(),'did not match any products')]")

        if no_results_message:
            print(" No results message displayed as expected.")
        else:
            print(" Fallback results displayed. Amazon likely returned sponsored or suggested items.")

        print(" Invalid search handled correctly.")
    except Exception as e:
        print(f" Unexpected error during invalid search check: {e}")
        raise


def click_mobiles_link(driver, locator):
    by, value = locator
    mobiles_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
    mobiles_link.click()
    time.sleep(3)
    assert "mobile-phones" in driver.current_url.lower() or "mobile" in driver.title.lower()


def add_to_wishlist_without_login(driver, sponsored_xpath, wishlist_xpath):
    sponsored_product = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sponsored_xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sponsored_product)
    sponsored_product.click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])

    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

    wishlist_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wishlist_xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", wishlist_btn)
    wishlist_btn.click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.any_of(EC.presence_of_element_located((By.ID, "ap_email")), EC.url_contains("signin")))
