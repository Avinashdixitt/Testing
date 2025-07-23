from selenium import webdriver

from selenium.webdriver.common.by import By
import time
#driver-webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


driver=webdriver.Chrome()


# driver.implicitly_wait(10) # seconds # implicit woit
#
# driver.get("https://www.google.com/")
#
# driver.maximize_window()
#
# searchbox=driver.find_element(By.NAME,'g')
#
# searchbox.send_keys("Selenium")
#
# searchbox.submit()
# driver.find_element(By.XPATH, "//h3 [text()='Selenium']").click()
#
# driver.quit()
#=======================Explicit wait=======================================================
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Assume driver is your WebDriver instance
# wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
#
# element = wait.until(
#     EC.presence_of_element_located((By.ID, "myElementId"))
# )
