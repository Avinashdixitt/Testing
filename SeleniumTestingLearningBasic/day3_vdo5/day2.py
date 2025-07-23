from selenium import webdriver

from selenium.webdriver.common.by import By
import time
#driver-webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


driver=webdriver.Chrome()

driver.get("https://www.facebook.com/")

time.sleep(1)

#driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("Admin")

time.sleep(5)

#driver.find_element_by_id("txtPassword").send_keys("admin123")
#driver.find_element(By.NAME,"password").send_keys("admin123")



#driver.find_element_by_id("btnLogin").click()
#driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
#driver.find_element(By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()


# act_title=driver.title
#
# exp_title="OrangeHRM"
#
# if act_title==exp_title:
#     print("Login Test Passed")
#
# else:
#     print("Login Test Failed")
driver.close()
