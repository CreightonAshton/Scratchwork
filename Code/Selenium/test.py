# imports
from selenium import webdriver
import time

DRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')
time.sleep(5)
driver.quit()
