from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.facebook.com/")

driver.find_element(By.NAME, "email").send_keys("03239651454")
driver.find_element(By.ID, "pass").send_keys("21334..12")
login = driver.find_element(By.NAME, 'login')
login.click()