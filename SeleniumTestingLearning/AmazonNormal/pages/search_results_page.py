from selenium.webdriver.common.by import By

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_result_count(self):
        results = self.driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot > div[data-component-type='s-search-result']")
        return len([r for r in results if r.is_displayed()])
