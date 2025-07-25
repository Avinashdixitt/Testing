from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")

driver.maximize_window()

#Login

driver.find_element(By.ID,"txtUsername").send_keys("Admin")

driver.find_element(By.ID,"txtPassword").send_keys("admin123")

driver.find_element(By.ID, "btnLogin").click()

time.sleep(3)

#Admin-->user management-->users

admin=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b")

usermgmt=driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']")

users=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")

act=ActionChains(driver)

act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()