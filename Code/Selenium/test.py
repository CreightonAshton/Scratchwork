# imports
from selenium import webdriver
import time

DRIVER_PATH = '/Users/Creighton/anaconda3/bin'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')
time.sleep(5)
driver.quit()
