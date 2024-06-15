import pytest

import pytest_demo
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def launch_browser():
    serv_obj = Service("C:\\chromedriver.exe")
    global driver
    driver = webdriver.Chrome(service=serv_obj)
    yield
    driver.quit()


def test_url(launch_browser):
    driver.get("https://adactinhotelapp.com/")
    print(driver.current_url)
    driver.get_screenshot_as_file('homepage.png')
