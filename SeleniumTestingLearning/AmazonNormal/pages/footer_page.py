from selenium.webdriver.common.by import By

class FooterPage:
    def __init__(self, driver):
        self.driver = driver

    def get_footer_links(self):
        footer_links = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'navFooterVerticalRow')]//a")
        return [link.text.strip() for link in footer_links if link.text.strip()]
