from selenium import webdriver

from selenium.webdriver.common.by import By
import time
#driver-webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")

emailbox=driver.find_element(By. XPATH,"//input[@id='Email']")



emailbox.clear()

emailbox.send_keys("abc@gmail.com")



print("result of text:",emailbox.text) # printed nothing

print("result of get_attribute():",emailbox.get_attribute('value'))

#abc@gmail.com

# button=driver.find_element(By.XPATH,"//button [normalize-space()='Log in']")
#
# print("result of text:", button.text)
#
# print("result of get_attribute():", button.get_attribute('value'))
# print("result of get_attribute():", button.get_attribute('type'))