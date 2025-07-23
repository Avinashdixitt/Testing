from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def apply_price_filter(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        lower_slider = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[id='p_36/range-slider_slider-item_lower-bound-slider']")
        ))
        self.actions.click_and_hold(lower_slider).move_by_offset(50, 0).release().perform()

        upper_slider = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[id='p_36/range-slider_slider-item_upper-bound-slider']")
        ))
        self.actions.click_and_hold(upper_slider).move_by_offset(-100, 0).release().perform()