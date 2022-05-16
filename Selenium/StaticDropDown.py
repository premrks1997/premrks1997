from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(r'D:\chromedriver_win32 (3)\chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
driver.find_element(By.ID, "dropdown-class-example").click()
dropdown.select_by_value("option1")
dropdown.select_by_visible_text("Option2")