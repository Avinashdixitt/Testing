from selenium import webdriver

#rom selenium.webdriver.chrome.service import Service

ops=webdriver.ChromeOptions()

ops.add_argument("--disable-notificatins")
driver=webdriver.Chrome()

#serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver=webdriver.Chrome(options=ops)

driver.get("https://whatmylocation.com/")

driver.maximize_window()