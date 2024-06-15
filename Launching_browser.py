import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get('http://google.com')
driver.maximize_window()
print(driver.title) #title of url
print(driver.current_url) # current url of browser opened
time.sleep(2)
