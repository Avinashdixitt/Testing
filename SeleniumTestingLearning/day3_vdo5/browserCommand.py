from selenium import webdriver

from selenium.webdriver.common.by import By
import time
#driver-webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


driver=webdriver.Chrome()


driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()
time.sleep(5)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)

#driver.close() #close the tab which was open first or where drive focus.
driver.quit() #it will kill all the process on browser and shut browser
time.sleep(5)
