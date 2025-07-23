from BasePage import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.click_element("#login-btn")  # using base method