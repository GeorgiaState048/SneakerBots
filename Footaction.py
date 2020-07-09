import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
shoeMarketName = "https://www.footaction.com/product/adidas-originals-nmd-r1-v2-mens/FY1255.html"
sMarketName = "https://www.footaction.com/account/login"
sUserName = "jonathanlaurent754@gmail.com"
sPassword = "Jonathan!013"
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
        email.send_keys(sUserName)
        aBrowserDriver.find_element_by_xpath("//input[contains(@type, 'password')]").send_keys(sPassword)
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

    # choosing size (Possibly change this to let me choose the size)
    element1 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, '//label[contains(@for, "input_radio_size_090")]')))
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
    element13.send_keys(cvv)

    aBrowserDriver.switch_to.default_content()

    element16 = WebDriverWait(aBrowserDriver, timeToWait).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Place Order"]')))
    print("Checkout Button Found")
