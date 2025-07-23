from selenium import webdriver
from methods import *

def assignment():
    driver= webdriver.Chrome()
    driver.get("https://rtc-automation.netlify.app/")
    driver.maximize_window()
    loginpage(driver)
    tablepage(driver)
    namepage(driver)
    datepage(driver)
    dropdownpage(driver)
    fileuploadpage(driver)
    modalpage(driver)
    alertpage(driver)
    promptpage(driver)
    xpathpage(driver)
    downloadpage(driver)
    selectorpage(driver)
    shadowdompage(driver)
    driver.quit()


assignment()
