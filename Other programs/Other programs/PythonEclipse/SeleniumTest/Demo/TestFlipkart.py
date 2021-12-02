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
driver.get("https://www.flipkart.com/")
driver.find_element_by_name("q").send_keys("shoes")
driver.find_element_by_css_selector("#container > div > div._1kfTjk > div._1rH5Jn > div._2Xfa2_ > div._1cmsER > form > div > button > svg").click()
time.sleep(2)
driver.find_element_by_css_selector("#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(3) > div > a > div:nth-child(1) > div > div > div > img").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()
time.sleep(2)



