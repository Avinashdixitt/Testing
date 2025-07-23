#Need to save a file with the name of Avinash Testing file.pdf at path C:\\Users\\Avinash Dixit\\OneDrive\\Desktop\\Avinash Testing file.pdf
#or make some changes in path loc 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rtc-automation.netlify.app/")
driver.maximize_window()
# for front page login page
try:
    driver.find_element(By.XPATH,"//input[@id='shub99']").send_keys("avinash.dixit@rtctek.com")
    driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("Qwsa@123")
    driver.find_element(By.XPATH,"//input[@placeholder='Enter your company']").send_keys("RTCTEK")
    driver.find_element(By.XPATH,"//input[@placeholder='Enter your mobile number']").send_keys("9876543212")
    driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
    print("Pass 1")
    time.sleep(2)
except Exception as e:
    print("failed 1:", e)
time.sleep(2)


try:
    #for 2nd page table marking
    driver.find_element(By.XPATH,"//input[@id='ohrmList_chkSelectAll']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
    time.sleep(2)
    print("Pass 2")
except Exception as e:
    print("failed 2:", e)
time.sleep(2)

try:
    #3rd page for activate first,last name option then filling
    driver.find_element(By.XPATH,"//label[normalize-space()='Can you enter name here through automation']//*[name()='svg']").click()
    driver.find_element(By.XPATH,"//input[@placeholder='First Enter name']").send_keys("Avinash")
    driver.find_element(By.XPATH,"//input[@placeholder='Enter Last name']").send_keys("Dixit")
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
    time.sleep(2)
    print("Pass 3")
except Exception as e:
    print("failed 3:", e)
time.sleep(2)

#4th page for date selection
#driver.find_element(By.XPATH,"//label[normalize-space()='Can you enter name here through automation']//*[name()='svg']").click()
try:
    date_input = driver.find_element(By.CSS_SELECTOR, "input[name='the_date']")
    date_to_select = "25-06-2025"
    date_input.send_keys(date_to_select)
    print(f"Pass 4: {date_to_select}")
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
except Exception as e:
    print("failed:4", e)
time.sleep(2)

try:
    # 5th for selecting from dropdown
    dropdown=Select(driver.find_element(By.XPATH,"//select[@id='cars']"))
    dropdown.select_by_value("volvo")
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
    time.sleep(2)
    print("Pass 5")
except Exception as e:
    print("failed 5:", e)
time.sleep(2)

#6th for  uploading file
try:
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_path = "C:\\Users\\Avinash Dixit\\OneDrive\\Desktop\\Avinash Testing file.pdf"

    file_input.send_keys(file_path)
    print("pass 6.")
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
except Exception as e:
    print("failed 6:", e)
time.sleep(2)

try:
    #7th for open model automation

    driver.find_element(By.XPATH,"//button[normalize-space()='Open Modal']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[@class='close']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
    time.sleep(2)
    print("pass 7")
except Exception as e:
    print("failed 7:", e)
time.sleep(2)

try:
    # 8th for notification
    driver.find_element(By.XPATH,"//button[normalize-space()='Show Confirmation']").click()
    alertwindow=driver.switch_to.alert
    alertwindow.accept()
    time.sleep(1)
    alertwindow.accept()
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
    print("pass 8")
except Exception as e:
    print("failed 8:", e)
time.sleep(2)

try:
    #9th for prompt
    driver.find_element(By.XPATH,"//button[normalize-space()='Show Prompt']").click()
    alertwindow=driver.switch_to.alert
    alertwindow.send_keys("welcome")
    alertwindow.accept()
    alertwindow.accept()
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()

    print("pass 9")
except Exception as e:
    print("failed 9:", e)
time.sleep(2)

try:
    # 10 for xpath
    driver.find_element(By.XPATH,"//button[normalize-space()='Open XPath Practice Page']").click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.switch_to.window(tabs[0])
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
except Exception as e:
    print("failed 10:", e)
time.sleep(2)

try:

    # 11 for download
    driver.find_element(By.XPATH,"//button[normalize-space()='Download File']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
    time.sleep(1)
except Exception as e:
    print("failed 11:", e)
time.sleep(2)


try:
    # 12 for xpath
    driver.find_element(By.XPATH,"//input[@placeholder='Enter XPath or CSS Selector']").click()
    driver.find_element(By.XPATH,"//input[@placeholder='Enter XPath or CSS Selector']").send_keys("//li[normalize-space()='Item 1']")
    driver.find_element(By.XPATH,"//button[normalize-space()='Test']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
    time.sleep(2)
except Exception as e:
    print("failed 12:", e)
time.sleep(2)

try:
    #13 for shadow and  frame
    # Step 1: Find the shadow host container (get iframe from inside it)
    shadow_host = driver.execute_script('return document.querySelector(".shadow-container")')
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

    # Step 2: Now locate the iframe inside shadow root
    iframe = driver.execute_script('return arguments[0].querySelector("iframe")', shadow_root)

    # Step 3: Switch to the iframe
    driver.switch_to.frame(iframe)
    #print("Switched into iframe inside Shadow DOM")

    # Step 4: Interact with elements inside the iframe (like input, button)
    input_box = driver.find_element(By.CSS_SELECTOR, "input")
    input_box.send_keys("Hello")
    button = driver.find_element(By.ID, "testButton")
    button.click()
    print("Button clicked")
    print("Input typed successfully")
    driver.switch_to.default_content()
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
    time.sleep(2)
except Exception as e:
    print("failed 13:", e)
time.sleep(2)


driver.close()