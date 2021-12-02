'''
Created on 24-Nov-2021

@author: MANJUSHA G P
'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("sample test case started")
driver = webdriver.Chrome("F:\SeleniumTest\Browsers\chromedriver.exe")
# driver=webdriver.firefox()
# driver=webdriver.ie()
# maximize the window size
driver.maximize_window()
# navigate to the url
driver.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")
# Login
driver.find_element_by_name("ctl00$MainContent$username").send_keys("Tester")
driver.find_element_by_name("ctl00$MainContent$password").send_keys("test")
driver.find_element_by_name("ctl00$MainContent$login_button").click()
time.sleep(2)
print(driver.title)
time.sleep(2)
# view all orders
# check all
driver.find_element_by_id("ctl00_MainContent_btnCheckAll").click()
time.sleep(2)
# uncheck all
driver.find_element_by_id("ctl00_MainContent_btnUncheckAll").click()
time.sleep(2)
# delete selected items
driver.find_element_by_id("ctl00_MainContent_orderGrid_ctl02_OrderSelector").click()
driver.find_element_by_id("ctl00_MainContent_orderGrid_ctl07_OrderSelector").click()
driver.find_element_by_id("ctl00_MainContent_btnDelete").click()
time.sleep(2)
# edit item name
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/div[3]/table/tbody/tr[7]/td[13]/input").click() 
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtName").clear()
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtName").send_keys("JK")
time.sleep(2)
driver.find_element_by_id("ctl00_MainContent_fmwOrder_UpdateButton").click()
time.sleep(2)
# view all product list
driver.find_element_by_link_text("View all products").click()
time.sleep(2)
# order item
driver.find_element_by_partial_link_text("Ord").click()
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtQuantity").send_keys("5")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtName").send_keys("Jack")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox2").send_keys("j k r villa")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox3").send_keys("Tvpm")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox4").send_keys("Kerala")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox5").send_keys("123")
time.sleep(2)
driver.find_element_by_id("ctl00_MainContent_fmwOrder_cardList_1").click()
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox6").send_keys("12345")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox1").send_keys("12/02/2024")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_InsertButton").click()
time.sleep(2)
print("sample test case stoped")
driver.close()