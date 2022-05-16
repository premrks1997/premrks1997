import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(r'D:\chromedriver_win32 (3)\chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get("http://3.110.88.201/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for i in countries:
    if i.text == "India":
        i.click()
        break
driver.close()