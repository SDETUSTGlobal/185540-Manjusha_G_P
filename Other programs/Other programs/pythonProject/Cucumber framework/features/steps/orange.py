import time

from OpenSSL.rand import status
from behave import *
from selenium import webdriver
@given('Launch chrome browser')
def openchrome(context):
    context.driver = webdriver.Chrome(executable_path="F://SeleniumTest//Browsers//chromedriver.exe")
@when('Open orange home page')
def openorange(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)
@then('verify logo is present')
def checklogo(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/img").is_displayed()
    assert status is True
@then('close browser')
def close(context):
    context.driver.close()
