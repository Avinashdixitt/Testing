from cart_page import CartPage
from signin_page import SignInPage

def test_checkout_without_login(driver):
    cart = CartPage(driver)
    signin = SignInPage(driver)
    cart.open_cart()
    time.sleep(2)
    cart.proceed_to_checkout()
    time.sleep(2)
    assert signin.is_login_page(), "Login page was not displayed"
