'''
Created on 24-Nov-2021

@author: MANJUSHA G P
'''
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("test case started")  
#open Google Chrome browser  
driver = webdriver.Chrome("F:\SeleniumTest\Browsers\chromedriver.exe")  
#maximize the window size  
driver.maximize_window()  
#delete the cookies  
driver.delete_all_cookies()  
#navigate to the url  
driver.get("https://www.myntra.com/")  
#identify the user name text box and enter the value  
driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/input").send_keys("palazzo")  
time.sleep(2) 
driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/a/span").click()
time.sleep(2)  
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/ul/li[1]/a/div[1]/div/div/div/picture/img").click()
time.sleep(2)
#size 
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/button").click()
time.sleep(2)
# add to bag
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[3]/div/div[1]").click()
time.sleep(2)
# go to bag
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[3]/div/a").click()
time.sleep(2)
driver.close()  
print("successfully completed")