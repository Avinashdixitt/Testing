from selenium import webdriver

from selenium.webdriver.common.by import By
import time
#driver-webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


driver=webdriver.Chrome()


driver.get("https://www.amazon.in/")
driver.get("https://www.snapchat.com/")

time.sleep(5)
driver.back()    #tab back through navigation
time.sleep(5)
driver.forward()     #tab forward through
time.sleep(5)
driver.refresh()            #tab forward through
time.sleep(5)
driver.close()
