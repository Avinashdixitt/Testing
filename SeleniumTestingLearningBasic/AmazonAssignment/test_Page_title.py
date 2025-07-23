import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver
driver = webdriver.Chrome()

try:
    # 1. Navigate to Amazon.in
    driver.get("https://www.amazon.in")

    # Maximize window for visibility
    driver.maximize_window()

    # 2. Assert the page title contains 'Amazon.in'
    assert "Amazon.in" in driver.title
    print("✅ Page title verified")

    # 3. Verify search box is visible
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    assert search_box.is_displayed()
    print("✅ Search box is visible")

    # 4. Verify "Sign In" button is visible
    sign_in_button = driver.find_element(By.ID, "nav-link-accountList")
    assert sign_in_button.is_displayed()
    print("✅ 'Sign In' button is visible")
####################################################################################################################
    # Navigate to Amazon.in

    # Search for "wireless mouse"
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("wireless mouse")
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load (use explicit wait in production)
    time.sleep(3)

    # Assert results are displayed
    results = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot > div[data-component-type='s-search-result']")
    assert len(results) > 0
    print(f"✅ Search results found: {len(results)}")

    # Check that at least 10 results are visible
    visible_results = [r for r in results if r.is_displayed()]
    assert len(visible_results) >= 10
    print(f"✅ At least 10 results are visible: {len(visible_results)}")


finally:
    # Cleanup: close the browser
    driver.quit()
