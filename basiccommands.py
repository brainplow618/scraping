from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\seleniumPython\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# service_obj = Service("chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.facebook.com")
#
# print(driver.title)