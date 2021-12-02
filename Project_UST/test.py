import time
from selenium import webdriver
driver = webdriver.Chrome("D:\Software\chromedriver.exe")
driver.get("http://127.0.0.1:5000/")
print("Test is started")
driver.maximize_window()
driver.find_element_by_name('fname').send_keys('Manjusha')
driver.find_element_by_name('lname').send_keys('G P')
driver.find_element_by_name('emp_id').send_keys('185540')
driver.find_element_by_name('com_name').send_keys('UST')
driver.find_element_by_name('mail').send_keys('185540@ust-global.com')
time.sleep(2)
driver.find_element_by_xpath('/html/body/form/button').click()
time.sleep(5)
print("Test is finished successfully")
driver.close()


