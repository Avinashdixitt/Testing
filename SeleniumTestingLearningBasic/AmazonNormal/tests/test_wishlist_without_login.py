from home_page import HomePage
from product_page import ProductPage
from signin_page import SignInPage
import time

def test_wishlist_without_login(driver):
    driver.delete_all_cookies()
    home = HomePage(driver)
    home.load()
    home.search("mobile")
    time.sleep(3)
    driver.find_elements_by_css_selector(".s-title-instructions-style a")[0].click()
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)
    product = ProductPage(driver)
    product.click_wishlist()
    time.sleep(3)
    signin = SignInPage(driver)
    assert signin.is_login_page()