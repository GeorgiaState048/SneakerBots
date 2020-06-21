import time
import datetime

import openpyxl
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#sMarketName = "https://www.nike.com/launch" #Feed
#sMarketName = "https://www.nike.com/launch?s=upcoming" #Upcoming
#sMarketName = "https://www.nike.com/launch?s=in-stock" #In Stock
sMarketName = "https://www.nike.com/launch/t/air-force-1-added-air"
sUserName = "jonathanlaurent754@gmail.com"
sPassword = "Jonathan013"
timeToWait = 30 * 24 * 60 * 60  #30 days




#if __name__ == '__main__':
executable_path = "C:\\Program Files\\ChromeDriver\\chromedriver.exe"
chrome_options = Options()
#chrome_options.add_extension('C:\\Users\\psingirikonda1\\Downloads\\SetupVPN-Lifetime-Free-VPN-Уеб-магазин-на-Chrome_v3.7.0.crx')
aBrowserDriver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
aBrowserDriver.maximize_window()
aBrowserDriver.get(sMarketName)
time.sleep(5)

#Login to SNKRS
#Need to change code to login first
"""def Login():
    aBrowserDriver.find_element_by_xpath('//button[text()="Join / Log In"]').click()
    aBrowserDriver.find_element_by_xpath("//input[contains(@name, 'emailAddress')]").send_keys(sUserName)
    aBrowserDriver.find_element_by_xpath("//input[contains(@name, 'password')]").send_keys(sPassword)
    aBrowserDriver.find_element_by_xpath("//input[contains(@value, 'SIGN IN')]").click()
    print("Login Successful")"""

def removeError():
    try:
        element2 = WebDriverWait(aBrowserDriver, 5).until(EC.presence_of_element_located
                                                        ((By.XPATH, '//button[text()="OK"]')))
        aBrowserDriver.execute_script("arguments[0].click();", element2)
        print("Code Removed")
    except TimeoutException:#change to time is expired error
        print("Code is already removed")

#Login method after checkout is clicked
def Login():
    element0 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                               ((By.XPATH, "//input[contains(@name, 'emailAddress')]")))
    element0.send_keys(sUserName)
    aBrowserDriver.find_element_by_xpath("//input[contains(@name, 'password')]").send_keys(sPassword)
    aBrowserDriver.find_element_by_xpath("//input[contains(@value, 'MEMBER CHECKOUT')]").click()
    print("Login Successful")

#Check phone app for sizes
element = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.XPATH, '//button[text()="M 10 / W 11.5"]')))
print("element found")
#select size
aBrowserDriver.execute_script("arguments[0].click();", element)
#time.sleep(4)
print("Product Size Selected")

#Look for Buy button
#element1 = aBrowserDriver.find_element_by_xpath('//button[contains(@data-qa, "add-to-cart")]')
#print("element1 found")
#Add shoe to cart
#aBrowserDriver.execute_script("arguments[0].click();", element1)
#rint("Product added to cart")
#time.sleep(4)

#aBrowserDriver.find_element_by_xpath("//a[contains(@href, '/cart')]").click()
#time.sleep(4)
#element9 = aBrowserDriver.find_element_by_xpath('//button[text()="Checkout"]').click()
#print("element 9 found")
#aBrowserDriver.execute_script("arguments[0].click();", element9)
element9 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.element_to_be_clickable
                                                          ((By.XPATH, "//button[contains(@data-automation, 'checkout-button')]")))
#aBrowserDriver.find_element_by_xpath("//button[contains(@data-automation, 'checkout-button')]").click()
element9.click()
print("proceeding to checkout")
#time.sleep(4)

element0 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                           ((By.XPATH, "//input[contains(@name, 'emailAddress')]")))
element0.send_keys(sUserName)
aBrowserDriver.find_element_by_xpath("//input[contains(@name, 'password')]").send_keys(sPassword)
aBrowserDriver.find_element_by_xpath("//input[contains(@value, 'MEMBER CHECKOUT')]").click()
print("Login Successful")

removeError()

#time.sleep(4)

element3 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                          ((By.XPATH, '//button[text()="Continue to Payment"]')))
element3.click()

print("Continuing to Payment")
#element3 = aBrowserDriver.find_element_by_xpath('//button[text()="Continue to Payment"]')
#element3.click()

removeError()

time.sleep(2)
#Type in cvNumber automatically (Make a separate that doesnt do this just in case
#element87 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                           #((By.XPATH, "//input[contains(@placeholder, 'XXX')]")))

print("The search begins")
print("the")

iframe = WebDriverWait(aBrowserDriver, 5).until(EC.presence_of_element_located
                                                        ((By.XPATH, "//iframe[contains(@title, 'Credit Card CVV Form')]")))
print(iframe)
aBrowserDriver.switch_to.frame(iframe)

print("switched to iframe")

"""testElement = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.XPATH, '//h3[text()="SELECT PAYMENT METHOD")]')))
print("test element found")"""

element87 = aBrowserDriver.find_element_by_xpath("//input[contains(@placeholder, 'XXX')]")
print("element87 found")
element87.send_keys('894')

#aBrowserDriver.switch_to.default_content()
#print("switched to default content")s

element10 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                        ((By.XPATH, "//button[text()='Place Order')]")))

print("element10 found")

#click save and continue button

#time.sleep(4)
#element4 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                           #((By.XPATH, "//input[contains(@placeholder, 'XXX')]")))
#aBrowserDriver.find_element_by_xpath("//input[contains(@placeholder, 'XXX')]")
#print("element4 found")
#removeError()

#Click drop-down sign(Payment summary) (Make a separate one that doesnt have to click on the credit card because it
# didn't make me do that when the product was in stock)
#element5 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "va-sm-t pl7-sm pr0-sm")]')))
#aBrowserDriver.execute_script("arguments[0].click();", element5)

#Click save and continue (See above comment)
#aBrowserDriver.execute_script("arguments[0].click();", element4)

#Click Submit Order
#element6 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Submit Order"]')))
#aBrowserDriver.execute_script("arguments[0].click();", element6)
