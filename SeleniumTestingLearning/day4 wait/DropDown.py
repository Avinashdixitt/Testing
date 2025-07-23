from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#Serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver-webdriver.Chrome (service=serv_obj)
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
#time.sleep(15)

#grpcountry_ele=driver.find_element(By.XPATH, "//select[@id='country']']")

drpcountry=Select(driver.find_element(By.XPATH, "//select[@id='country']"))

#select option from the dropdown

#drpcountry.select_by_visible_text("France")
drpcountry.select_by_value("canada") #Argentina
time.sleep(5)

#drpcountry.select_by_index(13) # index

#copture all the option and print them
#for opt in alloptions:
# print(opt.text)

#select option from dropdown without using built-in method

# for opt in alloptions:
#     if opt.text=="India":
#         opt.click()
#         break

# alloptions=driver.find_elements (By.XPATH, '//*[@id="input-country"]/option')
#
# print(len(alloptions))