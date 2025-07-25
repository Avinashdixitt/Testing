from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SortPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def sort_by_low_to_high(self):
        sort_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "a-autoid-0-announce")))
        sort_btn.click()
        low_to_high_option = self.wait.until(EC.element_to_be_clickable((By.ID, "s-result-sort-select_1")))
        low_to_high_option.click()
