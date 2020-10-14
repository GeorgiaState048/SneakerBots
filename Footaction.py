import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import Variables

shoeMarketName = "https://www.footaction.com/product/adidas-originals-nmd-r1-v2-mens/FY1255.html"
sMarketName = "https://www.footaction.com/account/login"

timeToWait = 30 * 24 * 60 * 60  # 30 days
#Make it so that the page refreshes when the timer ends

if __name__ == '__main__':
    executable_path = "C:\\Program Files\\ChromeDriver\\chromedriver.exe"
    # chrome_options = Options()
    # chrome_options.add_extension('C:\\Users\\psingirikonda1\\Downloads\\SetupVPN-Lifetime-Free-VPN-Уеб-магазин-на-Chrome_v3.7.0.crx')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    aBrowserDriver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
    aBrowserDriver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    aBrowserDriver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    aBrowserDriver.maximize_window()
    aBrowserDriver.get(sMarketName)

    time.sleep(25)

    # Login to SNKRSs
    # Need to change code to login first

    def Login():
        email = WebDriverWait(aBrowserDriver, timeToWait).until(
            EC.element_to_be_clickable((By.XPATH, '//input[contains(@type, "email")]')))
        email.send_keys(Variables.sUserName)
        aBrowserDriver.find_element_by_xpath("//input[contains(@type, 'password')]").send_keys(Variables.sPassword)
        signIns = aBrowserDriver.find_elements_by_xpath("//button[text()='Sign In']")
        time.sleep(5)
        print("Login Successful")

    #aBrowserDriver.get(shoeMarketName)

    def removeError():
        try:
            element2 = aBrowserDriver.find_element_by_xpath('//button[text()="Dismiss this error"]')
            aBrowserDriver.execute_script("arguments[0].click();", element2)
            print("Code Removed")
        except NoSuchElementException:
            print("Code is already removed")

    # keeping the website signed in so I don't have to wait in line in the morning.
    x = 0
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current time = " + current_time)
    status = True
    while status == True:
        # staySigned = WebDriverWait(aBrowserDriver, timeToWait).until(
        # EC.element_to_be_clickable((By.XPATH, '//button[text()="Stay Signed In"]')))
        # aBrowserDriver.execute_script("arguments[0].click();", staySigned)
        # print("Sign in button clicked")
        # print(x)
        now1 = datetime.now()
        status = True
        # current_time1 = now1.strftime("%H%M%S")
        newTime = ""
        while status == True:
            now1 = datetime.now()
            current_time1 = now1.strftime("%H%M%S")
            try:
                staySigned = WebDriverWait(aBrowserDriver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//button[text()="Stay Signed In"]')))
                aBrowserDriver.execute_script("arguments[0].click();", staySigned)
                print("Sign in button clicked")
                print(current_time1)
            except TimeoutException:
                test2 = 0
            finally:
                newTime = current_time1
                # print(current_time1)

            current_time1 = int(current_time1)
            if (96000 - current_time1) < 600:
                print("time limit reached")
                status = False
        time.sleep(1)

    # choosing size (Possibly change this to let me choose the size)
    element1 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, '//label[contains(@for, "input_radio_size_105")]')))
    print("product sizes found")
    aBrowserDriver.execute_script("arguments[0].click();", element1)

    # adding product to cart
    element2 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Add To Cart"]')))
    print("add to cart button found")
    aBrowserDriver.execute_script("arguments[0].click();", element2)
    print("Product added to cart")

    #aBrowserDriver.get("https://www.footlocker.com/cart")
    aBrowserDriver.get("https://www.footaction.com/checkout")
    time.sleep(2)

    # Searching for name on card
    element12 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'c-form-field__indicator')))
    aBrowserDriver.execute_script("arguments[0].click();", element12)

    iframes = WebDriverWait(aBrowserDriver, timeToWait).until(EC.presence_of_element_located((By.CLASS_NAME, 'js-iframe')))
    print("iframes found")
    aBrowserDriver.switch_to.frame(iframes)
    print("switched to iframe for name on card")

    time.sleep(1)

    element13 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "encryptedSecurityCode")]')))
    print("CVV found")
    element13.send_keys(Variables.cvv)

    aBrowserDriver.switch_to.default_content()

    element16 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Place Order"]')))
    print("Checkout Button Found")
    aBrowserDriver.execute_script("arguments[0].click();", element16)
    print("PRODUCT BOUGHT")
