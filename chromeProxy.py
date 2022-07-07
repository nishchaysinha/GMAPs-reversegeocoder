# Import the library Selenium
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform
import random
import socks5Proxy

def reverseGeocoder(lat,lng):
    # Make browser open in background
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('--allow-insecure-localhost')
    #options.add_argument('acceptInsecureCerts')
    #options.add_argument('--ignore-certificate-errors')
    options.add_argument('--proxy-server=' + random.choice(socks5Proxy.proxy)) #causes Certificate error because of a locally verified certificate

    # Create the webdriver object
    if platform.system()=="Windows":
        browser = webdriver.Chrome(
            executable_path="drivers/chromedriver.exe", options=options)

    elif platform.system()=="Darwin":
        browser = webdriver.Chrome(
            executable_path="/usr/local/bin/chromedriver", options=options)

    else:
        print("Linux Detected, Currently Doesn't support Linux")

    # Obtain the Google Map URL
    url = "http://maps.google.com/maps?z=12&t=m&q=loc:"+lat+"+"+lng
    # Open the Google Map URL
    browser.get(url)
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "LCF4w")))
    title = browser.find_element(By.CLASS_NAME, "LCF4w")

    return title.text

x=reverseGeocoder("17.380855791871582", "78.50671337782575")
print(x)