from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Step 1: Open Amazon.in
    driver.get("https://www.amazon.in")

    # Step 2: Search for "power bank"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("power bank")
    search_box.send_keys(Keys.RETURN)

    # Step 3: Wait & sort by Price: Low to High
    time.sleep(5)

    sort_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "a-autoid-0-announce"))
    )
    sort_btn.click()

    low_to_high_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "s-result-sort-select_1"))
    )
    low_to_high_option.click()

    print("✅ Sorted by Price: Low to High")
    time.sleep(5)

    # Step 4: Scroll down to force lazy content rendering
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(3)

    # Step 5: Try to read prices using textContent instead of .text
    price_elements = driver.find_elements(By.CSS_SELECTOR, "span.a-price > span.a-offscreen")

    valid_prices = []
    for elem in price_elements:
        price_text = elem.get_attribute("textContent").strip().replace("₹", "").replace(",", "")
        if price_text.replace(".", "").isdigit():
            valid_prices.append(float(price_text))
        if len(valid_prices) == 2:
            break

    if len(valid_prices) < 2:
        raise Exception("❌ Could not find at least 2 valid prices.")

    price1, price2 = valid_prices[0], valid_prices[1]
    print(f"💰 First Price: ₹{price1}, Second Price: ₹{price2}")
    assert price1 <= price2, "❌ Price order is incorrect!"
    print("✅ First product price is less than or equal to second.")

finally:
    driver.quit()
