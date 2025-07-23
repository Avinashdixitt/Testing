from home_page import HomePage
from footer_page import FooterPage
import time

def test_footer_links(driver):
    home = HomePage(driver)
    home.load()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    footer = FooterPage(driver)
    links = footer.get_footer_links()
    expected = ["About Amazon", "Careers", "Press Releases", "Amazon Science", "Sell on Amazon"]
    for link in expected:
        assert link in links, f"Missing footer link: {link}"