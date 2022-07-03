# Import the library Selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import platform

# Make browser open in background
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Create the webdriver object
if platform.system()=="Windows":
    browser = webdriver.Chrome(
        executable_path="C:\chromedriver_win32\chromedriver.exe", options=options)

elif platform.system()=="Darwin":
    browser = webdriver.Chrome(
        executable_path="/usr/local/bin/chromedriver", options=options)

else:
    print("Linux Detected, Currently Doesn't support Linux")

lat="28.549819596259738"
lng="77.3659236434599"

lat=str(input("enter lat: "))
lng=str(input("enter long: "))

# Obtain the Google Map URL
url = "http://maps.google.com/maps?z=12&t=m&q=loc:"+lat+"+"+lng


# Open the Google Map URL
browser.get(url)


WebDriverWait(browser, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "LCF4w")))


# Obtain the title of that place
title = browser.find_element(By.CLASS_NAME, "LCF4w")
print(title.text)

'''
# Obtain the ratings of that place
stars = browser.find_element(By.CLASS_NAME, "aMPvhf-fI6EEc-KVuj8d")
print("The stars of restaurant are:", stars.text)
print("\n")
'''

