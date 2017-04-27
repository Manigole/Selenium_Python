# Import the Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# open Firefox
driver = webdriver.Firefox()
print(' firefox Opens !! ')
# open Namaste url in Firefox
driver.maximize_window()
print(' firefox  maximizes!! ')
driver.get("http://namaste.net")
print(' Namaste website opens !!')

##---find login link/text

driver.find_elements_by_xpath('*//*[text()="Log In"]')
print(' login Link Found!! ')

##--click login link

elm = driver.find_element_by_link_text("Log In")
elm.click()
print('Login Link Clicked...link redirecting to Login page !! ')

##---Land to Login page

driver.find_elements_by_xpath('*//*[text()="Member Login"]')
print(' Landed to login Page !! ')

##--User
user = "mani"

# Password
pwd = "Email#123"

# Initialize


inputElement=driver.find_element_by_id("MemberLoginForm")
inputElement.send_keys(user)

# Enter Password
inputElement = driver.find_element_by_id("MemberLoginPass")
inputElement.send_keys(pwd)


elm = driver.find_element_by_link_text("MemberLoginButton")
elm.click()

elem.send_keys(Keys.RETURN)


