import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_verify_five_footer_links(driver):
    wait = WebDriverWait(driver, 20)

    print("🚀 Opening Amazon.in")
    driver.get("https://www.amazon.in")
    time.sleep(2)

    print("⬇️ Scrolling to footer")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    print("🔍 Collecting footer links")
    footer_links_xpath = "//div[contains(@class, 'navFooterVerticalRow')]//a"
    footer_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, footer_links_xpath)))

    # Collect visible link texts
    link_texts = [link.text.strip() for link in footer_links if link.text.strip() != '']

    print("📋 All footer links found:")
    for text in link_texts:
        print("  -", text)

    # ✅ Updated expected links
    expected_links = [
        "About Amazon",          # Changed from "About Us"
        "Careers",
        "Press Releases",
        "Amazon Science",
        "Sell on Amazon"
    ]

    print("\n✅ Verifying required links are present:")
    missing_links = []
    for expected in expected_links:
        if expected in link_texts:
            print(f"  ✔ Found: {expected}")
        else:
            print(f"  ❌ Missing: {expected}")
            missing_links.append(expected)

    assert not missing_links, f"❌ These footer links were not found: {', '.join(missing_links)}"
    print("\n🎉 All required footer links are present!")
