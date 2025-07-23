from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")

driver.maximize_window()

#Login
time.sleep(5)


driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

time.sleep(3)
#Admin-->user management-->users

driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()

#driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']").click()

#driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']").click()
time.sleep(5)

#total rows n a table

# rows=len (driver.find_elements (By.XPATH,"//table [@id='resultTable']//tbody/tr"))
#
# print("total number of rows in a table:",rows)
#
# count=0
#
# for r in range(1,rows+1):
#     status=driver.find_element(By.XPATH,"//table [@id='resultTable']/tbody/tr["+str(r)+"]/td[5]").text
#     if status=="Enabled":
#         count=count+1
#
# print("Total Number of users:",rows)
#
# print("Number of enabled users:", count)
#
# print("Number of disabled users:",(rows-count))