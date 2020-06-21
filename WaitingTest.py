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

#sMarketName = "https://www.nike.com/launch" #Feed
#sMarketName = "https://www.nike.com/launch?s=upcoming" #Upcoming
#sMarketName = "https://www.nike.com/launch?s=in-stock" #In Stock
sMarketName = "https://outlook.live.com/owa/?outlookhomepage=1&nlp=1"
sUserName = "jonathanlaurent13@hotmail.com"
sPassword = "Jonathan!013"
timeToWait = 30 * 24 * 60 * 60  #30 days




if __name__ == '__main__':
    executable_path = "C:\\Program Files\\ChromeDriver\\chromedriver.exe"
    chrome_options = Options()
    aBrowserDriver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
    aBrowserDriver.maximize_window()
    aBrowserDriver.get(sMarketName)
    time.sleep(5)

    #Login to Email
    def Login():
        element0 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                                   ((By.XPATH, "//input[contains(@name, 'loginfmt')]")))
        element0.send_keys(sUserName)

        element1 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                                   ((By.XPATH, "//input[contains(@value, 'Next')]")))
        aBrowserDriver.execute_script("arguments[0].click();", element1)

        element2 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                                   ((By.XPATH, "//input[contains(@id, 'i0118')]")))
        element2.send_keys(sPassword)

        element3 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located
                                                                   ((By.XPATH, "//input[contains(@value, 'Sign in')]")))
        #aBrowserDriver.execute_script("arguments[0].click();", element3)
        element3.click()
        print("Login Successful")

    Login()

    element4 = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@title, 'jonathanlaurent754@gmail.com')]")))
    WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, element4)))
    print("element4[1] is clickable")

    element4[1].click()