from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'D:\chromedriver_win32 (3)\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@target = '_blank']").click()
print(driver.window_handles)
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
print(driver.find_element(By.XPATH, "//h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element(By.XPATH, "//h3").text)
