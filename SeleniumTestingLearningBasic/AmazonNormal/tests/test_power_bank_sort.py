from home_page import HomePage
from sort_page import SortPage
import time

def test_power_bank_sort(driver):
    home = HomePage(driver)
    home.load()
    home.search("power bank")
    time.sleep(5)
    sorter = SortPage(driver)
    sorter.sort_by_low_to_high()
    time.sleep(5)