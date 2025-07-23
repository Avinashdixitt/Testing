from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Step 1: Open Amazon.in
    driver.get("https://www.amazon.in")

    # Step 2: Search for 'headphones'
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.clear()
    search_box.send_keys("headphones")
    search_box.send_keys(Keys.RETURN)

    time.sleep(4)

    # Step 3: Scroll to price slider section
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)

    # Step 4: Move the lower-bound slider right (to ₹500)
    lower_slider = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='p_36/range-slider_slider-item_lower-bound-slider']"))
    )
    actions = ActionChains(driver)
    actions.click_and_hold(lower_slider).move_by_offset(50, 0).release().perform()
    print("✅ Moved lower-bound price slider to ₹500")

    time.sleep(1)

    # Step 5: Move the upper-bound slider left (to ₹1000)
    upper_slider = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='p_36/range-slider_slider-item_upper-bound-slider']"))
    )
    actions.click_and_hold(upper_slider).move_by_offset(-100, 0).release().perform()
    print("✅ Moved upper-bound price slider to ₹1000")

    # Wait for filtered results to load
    time.sleep(6)

    # Step 6: Validate that product results exist
    results = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot > div[data-component-type='s-search-result']")
    print(f"✅ Found {len(results)} products after applying slider filter.")

finally:
    driver.quit()
