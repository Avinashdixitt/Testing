from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#drive.find_element(By.LINK_TEXT,'Digital downloads').click()
time.sleep(6)
links=driver.find_element(By.TAG_NAME,'a')
print(len(links))
