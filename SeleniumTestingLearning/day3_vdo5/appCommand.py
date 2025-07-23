from selenium import webdriver

from selenium.webdriver.common.by import By
import time
#driver-webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title) #OrangeHRM

print(driver.current_url) #https://opensource-demo.orangehrmlive.com/

print(driver.page_source)

driver.quit()