from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'D:\chromedriver_win32 (3)\chromedriver.exe')

driver = webdriver.Chrome(service=s)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH, "//div[@class = 'right-align']/fieldset/label/input")
print(len(checkboxes))
for i in checkboxes:
    i.click()
    assert i.is_selected()