from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.get("https://www.amazon.in/gp/cart/view.html")

    def proceed_to_checkout(self):
        self.driver.find_element(By.NAME, "proceedToRetailCheckout").click()