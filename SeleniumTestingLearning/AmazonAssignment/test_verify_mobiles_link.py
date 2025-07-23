import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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

def test_verify_mobiles_link(driver):
    # Step 1: Open Amazon.in
    driver.get("https://www.amazon.in/")
    time.sleep(2)

    # Step 2: Click on "Mobiles" link from top nav
    try:
        mobiles_link = driver.find_element(By.LINK_TEXT, "Mobiles")
        mobiles_link.click()
    except:
        pytest.fail("Mobiles link not found or not clickable")

    time.sleep(3)

    # Step 3: Assert URL or title
    current_url = driver.current_url.lower()
    page_title = driver.title.lower()

    assert (
        "mobile-phones" in current_url or "mobil" in page_title
    ), f"Navigation failed. URL: {current_url}, Title: {page_title}"
