'''
Created on 24-Nov-2021

@author: MANJUSHA G P
'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome("F:\SeleniumTest\Browsers\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()  
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("shoe")
time.sleep(2)
driver.find_element_by_id("nav-search-submit-button").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div/div/div[2]/div/span/a/div/img").click()
time.sleep(2)
driver.find_element_by_id("add-to-cart-button").click()
time.sleep(2)
driver.find_element_by_id("hlb-view-cart-announce").click()
time.sleep(2)
driver.close()  
print("successfully completed")



