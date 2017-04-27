# Import the Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# open Firefox
driver = webdriver.Firefox()
# open Namaste url in Firefox
driver.maximize_window()
driver.get("http://namaste.net")

##-----------------------------------

driver.find_elements_by_xpath('//a[@class="top"]')
print(' TC-1   Welcome to Namaste Test Pass!! ')

##-----------------------------------

driver.find_elements_by_xpath('//a[@class="top-in"]')
print(' TC-2   Join free link Test Pass!! ')

##-----------------------------------

driver.find_elements_by_xpath('//a[@class="left"]')
print(' TC-3   Log In link Test Pass!! ')

##-----------------------------------

driver.find_elements_by_xpath('//a[@class="Right"]')
print(' TC-4  My Cart link Test Pass!! ')

##-----------------------------------

driver.find_elements_by_xpath('//a[@class="gsearch"]')
print(' TC-5   Select Language present, Test Pass!! ')

##------------------------------------

driver.find_elements_by_xpath('//a[@class="logo"]')
print(' TC-6 Namaste Logo Present,  Test Pass!! ')

##-----------------------------------
driver.find_elements_by_xpath('//a[@class="search"]')
print(' TC-7 Search Box present , Test Pass!! ')

##------------------------------------
driver.find_elements_by_xpath('//a[@class="main"]')
print(' TC-8 Main Banner present, Test Pass!! ')

##------------------------------------

driver.find_elements_by_xpath('//a[@class="level-0"]')
print(' TC-9 Home Banner present, Test Pass!! ')

##------------------------------------

driver.find_elements_by_xpath('*//*[text()="HOME"]')
print(' TC-10 Home Button present, Test Pass!! ')
##------------------------------------

driver.find_elements_by_xpath('*//*[text()="NEW PRODUCTS"]')
print(' TC-11 NEW PRODUCTS Button present, Test Pass!! ')
##------------------------------------

driver.find_elements_by_xpath('*//*[text()="SHOPPING"]')
print(' TC-12 SHOPPING Button present, Test Pass!! ')

##------------------------------------

driver.find_elements_by_xpath('*//*[text()="OPEN STORE"]')
print(' TC-13 NEW PRODUCTS Button present, Test Pass!! ')
##------------------------------------

driver.find_elements_by_xpath('*//*[text()="FAQ"]')
print(' TC-14 FAQ Button present, Test Pass!! ')
##------------------------------------

driver.find_elements_by_xpath('*//*[text()="CONTACT US"]')
print(' TC-15 CONTACT US Button present, Test Pass!! ')
##------------------------------------

driver.find_elements_by_xpath('*//*[text()="About Us"]')
print(' TC-16 About Us Button present, Test Pass!! ')
##------------------------------------

driver.find_elements_by_xpath('*//*[text()="Payment"]')
print(' TC-17  Payment Button present, Test Pass!! ')
##------------------------------------

driver.find_elements_by_xpath('*//*[text()="Dispatch & Delivery"]')
print(' TC-18  Dispatch & Delivery Button present, Test Pass!! ')

##------------------------------------

driver.find_elements_by_xpath('*//*[text()="Refund & Return"]')
print(' TC-19  Refund & Return Button present, Test Pass!! ')
##------------------------------------

driver.find_elements_by_xpath('*//*[text()="Refund & Return"]')
print(' TC-20  Refund & Return Button present, Test Pass!! ')
##------------------------------------

driver.find_elements_by_xpath('*//*[text()="Customer Service"]')
print(' TC-21  Customer ServiceButton present, Test Pass!! ')


driver.close()