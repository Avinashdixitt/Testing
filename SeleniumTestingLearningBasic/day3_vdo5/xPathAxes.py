from selenium import webdriver

from selenium.webdriver.common.by import By
import time



driver=webdriver.Chrome()

driver.get("https://money.rediff.com/gainers")

time.sleep(1)


#avi=driver.find_element(By.XPATH, "//a[normalize-space()='STLTECH']").text
#self
#avi=driver.find_element(By.XPATH, "//a[normalize-space()='STLTECH']/self::a").text
 #self
#avi=driver.find_element(By.XPATH, "//a[normalize-space()='Bhaskar Agrochemical']/ancestor::tr").text
#print(avi)                                      #Bhaskar Agrochemical X 97.73 107.90 + 10.41 Buy  |  Sell

#child to parent(td named) to child(child of td as a)
#avi=driver.find_element(By.XPATH, "//a[normalize-space()='STLTECH']/parent::td//child::a").text
#print(avi)

#ancestor to child
# avi=driver.find_elements(By.XPATH, "//a[normalize-space()='Bhaskar Agrochemical']/ancestor::tr/child::td")
# print(len(avi))                         Bhaskar Agrochemical X 97.73 107.90 + 10.41 Buy  |  Sell
# 6


#descendant
# avi=driver.find_elements(By.XPATH, "//a[normalize-space()='Bhaskar Agrochemical']/ancestor::tr/descendant::*")
# print(len(avi))                     #10

#following
# following=driver.find_elements(By.XPATH, "//a[normalize-space()='Bhaskar Agrochemical']/ancestor::tr/following::*")
# print(len(following))                   #13435

#following-sibling
# followingsibli=driver.find_elements(By.XPATH, "//a[normalize-space()='Bhaskar Agrochemical']/ancestor::tr/following-sibling::*")
# print(len(followingsibli)) #1224

#preceding
# preceding=driver.find_elements(By.XPATH, "//a[normalize-space()='Bhaskar Agrochemical']/ancestor::tr/preceding::*")
# print(len(preceding))               #546

#preceding-sibling
precedingsib=driver.find_elements(By.XPATH, "//a[normalize-space()='Bhaskar Agrochemical']/ancestor::tr/preceding-sibling::*")
print(len(precedingsib))                        #6
driver.close()