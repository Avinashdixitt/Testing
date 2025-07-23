class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    def is_login_page(self):
        return "signin" in self.driver.current_url or "ap_email" in self.driver.page_source