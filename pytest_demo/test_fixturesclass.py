import time

import pytest
from selenium.webdriver.support.select import Select

import pytest_demo
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def launch_browser(request):
    serv_obj = Service("C:\\chromedriver.exe")
    request.cls.driver = webdriver.Chrome(service=serv_obj)
    yield
    request.cls.driver.quit()


@pytest.mark.usefixtures("launch_browser")
class Test_website:
    def test_url(self):
        self.driver.get("https://adactinhotelapp.com/")
        print(self.driver.current_url)
        self.driver.get_screenshot_as_file('homepage.png')

    def test_login(self):
        self.driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("Satish5201")
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("Satish5201")
        self.driver.find_element(By.XPATH, '//input[@type="Submit"]').click()
        # self.driver.get_screenshot_as_file("loggedin.jpg")

    def test_select_page(self):
        Location = Select(self.driver.find_element(By.ID, "location"))
        Location.select_by_index(1)
        Hotel = Select(self.driver.find_element(By.CSS_SELECTOR, "#hotels"))
        Hotel.select_by_index(2)
        Room_type = Select(self.driver.find_element(By.NAME, "room_type"))
        Room_type.select_by_index(3)
        number_of_rooms = Select(self.driver.find_element(By.NAME, "room_nos"))
        number_of_rooms.select_by_index(1)
        # driver.save_screenshot("Homepage.png")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        # time.sleep(5)
    def test_select_hotel_page(self):
        select_url = self.driver.current_url
        web_url = "https://adactinhotelapp.com/SelectHotel.php"
        assert web_url == select_url
        if web_url == select_url:
            print("u r in correct web page")

        select_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='radio']")
        select_button.click()
        select_button.is_selected()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(5)
    def test_pre_payment_page(self):
        print(self.driver.current_url)
        final_price = self.driver.find_element(By.NAME, "final_price_dis").get_attribute("value")
        print(final_price)
