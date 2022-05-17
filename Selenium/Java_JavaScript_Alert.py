from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'D:\chromedriver_win32 (3)\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
var = "option3"
driver.find_element(By.XPATH, "//input[@placeholder = 'Enter Your Name']").send_keys(var)
driver.find_element(By.XPATH, "//input[@placeholder = 'Enter Your Name']/following-sibling::input[@type='submit'][1]").click()
alert = driver.switch_to.alert
alert_Text = alert.text
assert var in alert_Text
alert.accept()