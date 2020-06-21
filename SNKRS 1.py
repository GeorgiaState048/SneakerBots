import time
import datetime
"""
Send Keys
Save/Continue
Submit
"""
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

#sMarketName = "https://www.nike.com/launch" #Feed
#sMarketName = "https://www.nike.com/launch?s=upcoming" #Upcoming
#sMarketName = "https://www.nike.com/launch?s=in-stock" #In Stock
sMarketName = "https://www.nike.com/launch/t/adapt-auto-max-anthracite"
sUserName = "jonathanlaurent754@gmail.com"
sPassword = "Jonathan013"
timeToWait = 30 * 24 * 60 * 60  #30 days




if __name__ == '__main__':
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
            element2 = aBrowserDriver.find_element_by_xpath('//button[text()="OK"]')
            aBrowserDriver.execute_script("arguments[0].click();", element2)
            print("Code Removed")
        except NoSuchElementException:
            print("Code is already removed")

    #Login method after checkout is clicked
    def Login():
        element0 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                                   ((By.XPATH, "//input[contains(@name, 'emailAddress')]")))
        element0.send_keys(sUserName)
        aBrowserDriver.find_element_by_xpath("//input[contains(@name, 'password')]").send_keys(sPassword)
        aBrowserDriver.find_element_by_xpath("//input[contains(@value, 'SIGN IN')]").click()
        print("Login Successful")

    #Check phone app for sizes
    element = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.XPATH, '//button[text()="M 9 / W 10.5"]')))
    print("element found")
    #select size
    aBrowserDriver.execute_script("arguments[0].click();", element)
    #time.sleep(4)
    print("Product Size Selected")

    #Look for Buy button
    element1 = aBrowserDriver.find_element_by_xpath('//button[contains(@data-qa, "feed-buy-cta")]')
    print("element1 found")
    #Add shoe to cart
    aBrowserDriver.execute_script("arguments[0].click();", element1)
    print("Moving to Login Page")

    Login()

    #time.sleep(4)

    removeError()

    #Type in cvNumber automatically (Make a separate that doesnt do this just in case
    element3 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.XPATH, '//button[contains(@id, "cvNumber")]')))
    print("element3 found")
    element3.send_keys('894')

    #click save and continue button
    element4 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.XPATH, '//button[contains(@data-qa, "save-button")]')))
    aBrowserDriver.execute_script("arguments[0].click();", element4)
    print("Credit card information saved")

    removeError()

    #Click Submit Order
    #element6 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Submit Order"]')))
    #aBrowserDriver.execute_script("arguments[0].click();", element6)
