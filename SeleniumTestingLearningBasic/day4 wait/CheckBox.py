from selenium import webdriver

from selenium.webdriver.common.by import By
import time
#driver-webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


driver=webdriver.Chrome()
#1) select specific checkbox

#driver.find_element(By.XPATH,"//input[@id='monday']").click()

#2) select all the checkboxes
driver.get("https://itera-qa.azurewebsites.net/home/automation")

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")


print(len(checkboxes)) #7

#Approoch1

#for i in range(len(checkboxes)):

# checkboxes[i].click()

#Approoch2

for checkbox in checkboxes:
    checkbox.click()

#3)clearing all the check boxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

#driver.quit(