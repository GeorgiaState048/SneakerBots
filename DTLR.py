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
#https://shopnicekicks.com/collections/recent-launch/products/nike-dunk-low-sp-university-red-mens-lifestyle-shoe-red-white
shoeMarketName = "https://www.dtlr.com/pages/releases"
sMarketName = "https://www.dtlr.com/account/login"
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
#Make it so that the page refreshes when the timer ends

if __name__ == '__main__':
    executable_path = "C:\\Program Files\\ChromeDriver\\chromedriver.exe"
    chrome_options = Options()
    # chrome_options.add_extension('C:\\Users\\psingirikonda1\\Downloads\\SetupVPN-Lifetime-Free-VPN-Уеб-магазин-на-Chrome_v3.7.0.crx')
    aBrowserDriver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
    aBrowserDriver.maximize_window()
    aBrowserDriver.get(sMarketName)


    #time.sleep(30)

    # Login to SNKRSs
    # Need to change code to login first
    def Login():
        aBrowserDriver.find_element_by_xpath("//input[contains(@name, 'customer[email]')]").send_keys(sUserName)
        aBrowserDriver.find_element_by_xpath("//input[contains(@name, 'customer[password]')]").send_keys(sPassword)
        aBrowserDriver.find_element_by_xpath("//button[contains(@name, 'btn_custom_login')]").click()
        print("Login Successful")

    Login()

    time.sleep(2)

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

    time.sleep(3)

    element0 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "nike-kyrie-6-usa-BQ4630-102")]')))
    print("Shoe Link Found")
    aBrowserDriver.execute_script("arguments[0].click();", element0)
    print("Moving to shoe page")

    #choosing size (Possibly change this to let me choose the size)
    element1 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.element_to_be_clickable((By.XPATH, '//label[contains(@for, "swatch-0-9")]')))
    print("Product size found")
    aBrowserDriver.execute_script("arguments[0].click();", element1)
    print("Product size selected")

    # adding product to cart
    element2 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "btn product-form__cart-submit")]')))
    print("add to cart button found")
    aBrowserDriver.execute_script("arguments[0].click();", element2)
    print("Product added to cart")

    element3 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@name, 'checkout')]")))
    print("checkout button found")
    aBrowserDriver.execute_script("arguments[0].click();", element3)
    print("moving to checkout")

    element4 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "First name")]')))
    print("First name found")
    element4.send_keys("Jonathan")

    element5 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Last name")]')))
    print("Last name found")
    element5.send_keys("Laurent")

    element6 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Address")]')))
    print("Address Found")
    element6.send_keys(sAddress)

    element7 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "City")]')))
    print("City Found")
    element7.send_keys("Suwanee")

    element8 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "ZIP code")]')))
    print("Zip code found")
    element8.send_keys(zipCode)

    element9 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Phone")]')))
    print("Phone Number found")
    element9.send_keys("")

    element10 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@id, 'continue_button')]")))
    print("continue to shipping button found")
    aBrowserDriver.execute_script("arguments[0].click();", element10)
    print("moving to shipping")

    element11 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@id, 'continue_button')]")))
    print("continue to payment button found")
    aBrowserDriver.execute_script("arguments[0].click();", element11)
    print("moving to payment")

    time.sleep(2)

    #switching to frames for each card info section

    iframes = aBrowserDriver.find_elements_by_class_name('card-fields-iframe')
    aBrowserDriver.switch_to.frame(iframes[0])
    print("switched to iframe for card number")

    element12 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Card number")]')))
    print("card number found")
    element12.send_keys(creditCard)

    aBrowserDriver.switch_to.default_content()

    #Searching for name on card

    iframes = aBrowserDriver.find_elements_by_class_name('card-fields-iframe')
    aBrowserDriver.switch_to.frame(iframes[1])
    print("switched to iframe for name on card")

    element13 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Name on card")]')))
    print("name on Card found")
    element13.send_keys("Jonathan Laurent")

    aBrowserDriver.switch_to.default_content()

    iframes = aBrowserDriver.find_elements_by_class_name('card-fields-iframe')
    aBrowserDriver.switch_to.frame(iframes[2])
    print("switched to iframe for expiry date")

    element14 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Expiration date (MM / YY)")]')))
    print("expiry date found")
    element14.send_keys("0922")

    aBrowserDriver.switch_to.default_content()

    iframes = aBrowserDriver.find_elements_by_class_name('card-fields-iframe')
    aBrowserDriver.switch_to.frame(iframes[3])
    print("switched to iframe for security code")

    element15 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Security code")]')))
    print("security code found")
    element15.send_keys(cvv)

    aBrowserDriver.switch_to.default_content()

    element16 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@id, "continue_button")]')))
    print("Checkout Button Found")