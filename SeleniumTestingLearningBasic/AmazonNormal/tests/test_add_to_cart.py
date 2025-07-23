

from AmazonNormal.pages.cart_page import CartPage
from product_page import ProductPage
import time

def test_add_to_cart(driver):
    home = HomePage(driver)
    home.load()
    home.search("keyboard")
    time.sleep(5)
    driver.find_elements_by_css_selector(".s-title-instructions-style a")[0].click()
    time.sleep(3)
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
    product = ProductPage(driver)
    product.click_add_to_cart()