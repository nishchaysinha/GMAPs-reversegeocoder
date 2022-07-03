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
        executable_path="chromedriver.exe", options=options)

elif platform.system()=="Darwin":
    browser = webdriver.Chrome(
        executable_path="/usr/local/bin/chromedriver", options=options)

else:
    print("Linux Detected, Currently Doesn't support Linux")


# Obtain the Google Map URL
url = "https://www.google.com/maps/@28.5123109,77.3799704,14z/data=!3m1!4b1!4m5!3m4!1s0x390ce88db913c975:0xbbec271e3ce71be1!8m2!3d28.5110359!4d77.3941312"


# Open the Google Map URL
browser.get(url)


WebDriverWait(browser, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "lMbq3e")))


# Obtain the title of that place
title = browser.find_element(By.CLASS_NAME, "lMbq3e")
print(title.text)

'''
# Obtain the ratings of that place
stars = browser.find_element(By.CLASS_NAME, "aMPvhf-fI6EEc-KVuj8d")
print("The stars of restaurant are:", stars.text)
print("\n")
'''

