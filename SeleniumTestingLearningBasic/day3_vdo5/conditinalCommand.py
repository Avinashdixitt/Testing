from selenium import webdriver

from selenium.webdriver.common.by import By
import time
#driver-webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")

driver.maximize_window()

#is_displayed() is enabled()

searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")

print("Display status:", searchbox.is_displayed())

print("Enabled status:", searchbox.is_enabled())
#is selected() for radio buttons and check boxes

rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")

rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("default radio buttons status.....")

print(rd_male.is_selected())

#Folse

print(rd_female.is_selected())

#False

rd_male.click() # select male radio button

print("After selecting male radio button.....")

print(rd_male.is_selected()) #True

print(rd_female.is_selected())

#False

rd_female.click()

print("After selecting fe-male radio button.....")

print(rd_male.is_selected())

#False

print(rd_female.is_selected())

#True
