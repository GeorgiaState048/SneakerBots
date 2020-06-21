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

# sMarketName = "https://www.nike.com/launch" #Feed
# sMarketName = "https://www.nike.com/launch?s=upcoming" #Upcoming
# sMarketName = "https://www.nike.com/launch?s=in-stock" #In Stock
sMarketName = "https://paymentcc.nike.com/services/cvv?id=ff169eaf-1687-470b-95fc-371c540c3f2a&ctx=checkout&language=undefined&maskerEnabled=true"
sUserName = "jonathanlaurent754@gmail.com"
sPassword = "Jonathan013"
timeToWait = 30 * 24 * 60 * 60  # 30 days

if __name__ == '__main__':
    executable_path = "C:\\Program Files\\ChromeDriver\\chromedriver.exe"
    chrome_options = Options()
    # chrome_options.add_extension('C:\\Users\\psingirikonda1\\Downloads\\SetupVPN-Lifetime-Free-VPN-Уеб-магазин-на-Chrome_v3.7.0.crx')
    aBrowserDriver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
    aBrowserDriver.maximize_window()
    aBrowserDriver.get(sMarketName)
    time.sleep(5)

    element87 = aBrowserDriver.find_element_by_xpath("//input[contains(@placeholder, 'XXX')]")
    print("element87 found")
    element87.send_keys('894')

    #This works