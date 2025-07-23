from home_page import HomePage
from filter_page import FilterPage
import time

def test_price_filter(driver):
    home = HomePage(driver)
    home.load()
    home.search("headphones")
    time.sleep(3)
    filter_page = FilterPage(driver)
    filter_page.apply_price_filter()
    time.sleep(5)