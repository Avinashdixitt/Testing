from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Step 1: Open Amazon
    driver.get("https://www.amazon.in")

    # Step 2: Search "keyboard"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("keyboard")
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for page to load

    # Step 3: Scroll to load product elements
    driver.execute_script("window.scrollBy(0, 400)")
    time.sleep(2)

    # Step 4: Click first product using your XPath
    product_xpath = "//div[@class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1']//div[@class='a-section a-spacing-none puis-padding-right-small s-title-instructions-style puis-desktop-list-title-instructions-style']"
    first_product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, product_xpath))
    )
    print("🛒 Clicking on the first product")
    first_product.click()

    # Step 5: Switch to product tab if opened
    time.sleep(3)
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])

    # Step 6: Click Add to Cart using your XPath
    add_to_cart_xpath = "//input[@id='add-to-cart-button']"
    add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath))
    )
    add_to_cart.click()
    print("✅ Added product to cart")

    # Step 7: Verify cart update (optional)
    time.sleep(3)
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nav-cart-count"))
    )
    count = int(cart_count.text.strip())
    assert count >= 1, "❌ Cart count did not increase!"
    print(f"✅ Cart updated. Count: {count}")

finally:
    driver.quit()
