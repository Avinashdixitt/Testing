from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.amazon.in")

    def search(self, keyword):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.submit()

    def is_sign_in_visible(self):
        return self.driver.find_element(By.ID, "nav-link-accountList").is_displayed()

    def click_mobiles_link(self):
        self.driver.find_element(By.LINK_TEXT, "Mobiles").click()