from home_page import HomePage
import time

def test_verify_mobiles_link(driver):
    home = HomePage(driver)
    home.load()
    home.click_mobiles_link()
    time.sleep(3)
    assert "mobile" in driver.current_url.lower() or "mobil" in driver.title.lower()