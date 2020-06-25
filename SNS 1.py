import time
import datetime

import openpyxl
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#try to login first
#Work on dismiss error
# sMarketName = "https://www.nike.com/launch" #Feed
# sMarketName = "https://www.nike.com/launch?s=upcoming" #Upcoming
# sMarketName = "https://www.nike.com/launch?s=in-stock" #In Stock
shoeMarketName = "https://www.sneakersnstuff.com/en/product/45050/adidas-yeezy-qntm-barium"
sMarketName = "https://www.sneakersnstuff.com/en/auth/view"
sUserName = "jonathanlaurent754@gmail.com"
sPassword = "Soccer!013"
sAddress = "118 Eastham Court"
zipCode = "30024"
City = "Suwanee"
phoneNumber = "4702469234"
creditCard = '5275190017799129'
expireMonth = '9'
expireYear = '22'
cvv = '894'

timeToWait = 30 * 24 * 60 * 60  # 30 days

if __name__ == '__main__':
    executable_path = "C:\\Program Files\\ChromeDriver\\chromedriver.exe"
    chrome_options = Options()
    # chrome_options.add_extension('C:\\Users\\psingirikonda1\\Downloads\\SetupVPN-Lifetime-Free-VPN-Уеб-магазин-на-Chrome_v3.7.0.crx')
    aBrowserDriver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
    aBrowserDriver.maximize_window()
    aBrowserDriver.get(sMarketName)

    # Login to SNKRSs
    # Need to change code to login first
    """def Login():
        aBrowserDriver.find_element_by_xpath('//button[text()="Join / Log In"]').click()
        aBrowserDriver.find_element_by_xpath("//input[contains(@name, 'emailAddress')]").send_keys(sUserName)
        aBrowserDriver.find_element_by_xpath("//input[contains(@name, 'password')]").send_keys(sPassword)
        aBrowserDriver.find_element_by_xpath("//input[contains(@value, 'SIGN IN')]").click()
        print("Login Successful")"""

    time.sleep(15)
    aBrowserDriver.get(shoeMarketName)
    def removeError():
        try:
            element2 = aBrowserDriver.find_element_by_xpath('//button[text()="Dismiss this error"]')
            aBrowserDriver.execute_script("arguments[0].click();", element2)
            print("Code Removed")
        except NoSuchElementException:
            print("Code is already removed")


    # Login method after checkout is click
    def Login():
        element0 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                                   ((By.XPATH,
                                                                     "//input[contains(@name, 'emailAddress')]")))
        element0.send_keys(sUserName)
        aBrowserDriver.find_element_by_xpath("//input[contains(@name, 'password')]").send_keys(sPassword)
        aBrowserDriver.find_element_by_xpath("//input[contains(@value, 'SIGN IN')]").click()
        print("Login Successful")


    #choosing size (Possibly change this to let me choose the size)
    elementT = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-sizes__label')))
    element1 = aBrowserDriver.find_elements_by_class_name('product-sizes__label')

    aBrowserDriver.execute_script("arguments[0].click();", element1[5])

    #adding product to cart
    element2 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@type, 'submit')]")))
    print("element2 found")
    #element2.click()
    aBrowserDriver.execute_script("arguments[0].click();", element2)
    print("moving to checkout slide")

    #moving to checkout page
    cart = "https://www.sneakersnstuff.com/en/cart/view"
    aBrowserDriver.get(cart)

    #typing in name
    element3 = aBrowserDriver.find_element_by_xpath("//input[contains(@id, 'first-name-input')]")
    print("element3 found")
    element3.send_keys("Jonathan")

    #typing in last name
    element4 = aBrowserDriver.find_element_by_xpath("//input[contains(@id, 'last-name-input')]")
    print("element4 found")
    element4.send_keys("Laurent")

    #typing in address
    element5 = aBrowserDriver.find_element_by_xpath("//input[contains(@id, 'address-line-2-input')]")
    print("element5 found")
    element5.send_keys(sAddress)

    #typing in zip code
    element6 = aBrowserDriver.find_element_by_xpath("//input[contains(@id, 'postal-code-input')]")
    print("element6 found")
    #element6.send_keys(zipCode)

    #typing in city
    element7 = aBrowserDriver.find_element_by_xpath("//input[contains(@id, 'city-input')]")
    print("element7 found")
    element7.send_keys(City)

    #typing in phone number
    element8 = aBrowserDriver.find_element_by_xpath("//input[contains(@id, 'phone-number-input')]")
    print("element8 found")
    element8.send_keys(phoneNumber)

    #switching to credit card number iframe
    WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
    iframes = aBrowserDriver.find_elements_by_tag_name('iframe')
    aBrowserDriver.switch_to.frame(iframes[0])
    print("switched to iframe for card number")

    element9 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "encryptedCardNumber")]')))
    print("card number found")
    element9.send_keys(creditCard)

    aBrowserDriver.switch_to.default_content()

    aBrowserDriver.switch_to.frame(iframes[1])
    print("switched to iframe for expiry month")

    element10 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "encryptedExpiryMonth")]')))
    print("expiry month found")
    element10.send_keys(expireMonth)

    aBrowserDriver.switch_to.default_content()

    aBrowserDriver.switch_to.frame(iframes[2])
    print("switched to iframe for expiry year")

    element11 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "encryptedExpiryYear")]')))
    print("expiry month found")
    element11.send_keys(expireYear)

    aBrowserDriver.switch_to.default_content()

    aBrowserDriver.switch_to.frame(iframes[3])
    print("switched to iframe for cvv")

    element12 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "encryptedSecurityCode")]')))
    print("cvv found")
    element12.send_keys(cvv)

    aBrowserDriver.switch_to.default_content()

    element13 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@name, "termsAccepted")]')))
    print("Terms and Conditions found")
    aBrowserDriver.execute_script("arguments[0].click();", element13)

    element14 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(@type, "submit")]')))
    print("Checkout Button Found")
    #aBrowserDriver.execute_script("arguments[0].click();", element14)
