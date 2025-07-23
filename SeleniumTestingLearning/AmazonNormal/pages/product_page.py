from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-button").click()

    def click_wishlist(self):
        self.driver.find_element(By.ID, "wishListMainButton").click()
