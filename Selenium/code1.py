import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(r'D:\chromedriver_win32 (3)\chromedriver.exe')

driver = webdriver.Chrome(service=s)

#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.get("http://3.110.88.201/dropdownsPractise/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
print(len(countries))
for i in countries:
    if i.text=="India":
        i.click()
        break

#driver.find_element(By.ID, "autocomplete").send_keys("Hello")
#driver.find_element(By.ID, "autocomplete").clear()
#dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
#driver.find_element(By.ID, "dropdown-class-example").click()
#dropdown.select_by_value("option1")
#driver.quit()
#driver.close()


