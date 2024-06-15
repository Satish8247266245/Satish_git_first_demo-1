import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
'''driver.get('https://www.flipkart.com/')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, '//img[@alt="Mobiles"]').click()
# driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/a[2]/div/div/div/div/img').click()
'''
driver.get('https://adactinhotelapp.com/')
driver.maximize_window()
driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("Satish5201")
driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("Satish5201")
driver.find_element(By.XPATH, '//input[@type="Submit"]').click()
#Homepage
Location = Select(driver.find_element(By.ID, "location"))
Location.select_by_index(1)
Hotel = Select(driver.find_element(By.CSS_SELECTOR, "#hotels"))
Hotel.select_by_index(2)
Room_type = Select(driver.find_element(By.NAME, "room_type"))
Room_type.select_by_index(3)
number_of_rooms = Select(driver.find_element(By.NAME, "room_nos"))
number_of_rooms.select_by_index(1)
# driver.save_screenshot("Homepage.png")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
# time.sleep(5)
select_url = driver.current_url
web_url = "https://adactinhotelapp.com/SelectHotel.php"
assert web_url == select_url
if web_url == select_url:
    print("u r in correct web page")

select_button = driver.find_element(By.CSS_SELECTOR, "input[type='radio']")
select_button.click()
select_button.is_selected()
driver.find_element(By.XPATH, "//input[@value='Continue']").click()
time.sleep(5)
print(driver.current_url)
final_price = driver.find_element(By.NAME, "final_price_dis").get_attribute("value")
print(final_price)

