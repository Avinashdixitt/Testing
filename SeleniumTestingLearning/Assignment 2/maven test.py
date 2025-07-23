from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set path to ChromeDriver

driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Accept Cookies if any (optional, depends on location)
try:
    accept_button = driver.find_element(By.XPATH, "//button[.='Accept all']")
    accept_button.click()
except:
    pass  # No popup

# Find the search input by XPath and type a query
search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")
search_box.send_keys("ChatGPT OpenAI")

# Press Enter to search
search_box.submit()

# Optional wait to view results
time.sleep(4)

# Close browser
driver.quit()
