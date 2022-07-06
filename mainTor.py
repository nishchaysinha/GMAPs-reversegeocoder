from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
def create_torbrowser_webdriver_instance():
  tor_binary_path_driver =  '/Users/XXX/Applications/TorBrowser.app/Contents/MacOS/firefox'
  geckodriver_path = 'drivers/geckodriver'

  os.popen(tor_binary_path_driver)
  options = Options()
  options.headless = True

  firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
  firefox_capabilities['proxy'] = {
      "proxyType": "MANUAL",
      'socksProxy': '127.0.0.1:9150',
      "socksVersion": 5
  }

  driver = webdriver.Firefox(capabilities=firefox_capabilities,
                             options=options,
                             executable_path=geckodriver_path)
  return driver