import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # Important: Clear cookies/session to simulate logged-out user
    driver.delete_all_cookies()

    yield driver
    driver.quit()


def test_wishlist_from_sponsored_product(driver):
    wait = WebDriverWait(driver, 20)

    print("🚀 Opening Amazon.in")
    driver.get("https://www.amazon.in/")

    print("🔍 Searching for 'mobile'")
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys("mobile")
    search_box.send_keys(Keys.RETURN)

    print("📦 Clicking on sponsored product")
    sponsored_xpath = (
        "//div[contains(@class, 's-widget-container') and .//span[text()='Sponsored']]"
        "//a[@class='a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal']"
    )
    sponsored_product = wait.until(EC.element_to_be_clickable((By.XPATH, sponsored_xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sponsored_product)
    sponsored_product.click()

    print("🗂 Switching to product tab")
    driver.switch_to.window(driver.window_handles[-1])

    print("❤️ Scrolling to and clicking on Add to Wishlist")
    try:
        wishlist_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='wishListMainButton']")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", wishlist_btn)
        time.sleep(2)

        try:
            wishlist_btn.click()
            print("✅ Clicked using standard click")
        except:
            print("⚠️ Standard click failed, using JS click")
            driver.execute_script("arguments[0].click();", wishlist_btn)

        print("🕒 Waiting for potential redirect...")
        time.sleep(5)

    except Exception as e:
        print(f"❌ Could not click wishlist button: {e}")
        driver.save_screenshot("wishlist_click_error.png")
        pytest.fail("Could not click Add to Wishlist button")

    # Logging current URL and title
    current_url = driver.current_url
    print(f"🌐 Current URL: {current_url}")
    print(f"📄 Page Title: {driver.title}")

    print("🔐 Verifying login or wishlist page...")
    try:
        login_detected = False

        try:
            WebDriverWait(driver, 10).until(
                EC.any_of(
                    EC.presence_of_element_located((By.ID, "ap_email")),
                    EC.presence_of_element_located((By.NAME, "email")),
                    EC.url_contains("signin")
                )
            )
            login_detected = True
            print("✅ Login form or URL detected.")
        except:
            if "wishlist" in current_url:
                print("⚠️ Redirected to Wishlist — you may already be logged in.")
            else:
                print("❌ Neither login nor wishlist redirect detected.")
                driver.save_screenshot("login_not_detected.png")
                pytest.fail("Login page did not appear, and no wishlist redirection detected.")

        assert login_detected or "wishlist" in current_url

    except Exception as e:
        print(f"❌ Unexpected error during login verification: {e}")
        driver.save_screenshot("unexpected_error.png")
        pytest.fail("Unexpected failure during login/wishlist page check.")
