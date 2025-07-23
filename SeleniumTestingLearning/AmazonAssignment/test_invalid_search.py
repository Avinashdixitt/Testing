import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_invalid_search_suggestions(driver):
    # Step 1: Open Amazon
    driver.get("https://www.amazon.in/")
    time.sleep(2)

    # Step 2: Search for gibberish
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("asdasdkjasdjasd")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Step 3: Check if search results (products) are shown
    try:
        # Product containers usually have 's-result-item' class
        product_results = driver.find_elements(By.XPATH,
                                               "//div[contains(@class, 's-result-item') and @data-component-type='s-search-result']")
        visible_results = [item for item in product_results if item.is_displayed()]

        assert len(visible_results) > 0, "No product suggestions or results were shown for gibberish input."
        print(f"✅ {len(visible_results)} products were suggested for gibberish input.")
    except Exception as e:
        pytest.fail(f"Error while checking for product suggestions: {str(e)}")
