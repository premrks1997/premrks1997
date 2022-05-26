from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service(r'D:\chromedriver_win32 (3)\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[text() = 'Shop']").click()
ele = driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")
for i in range(len(ele)):
    productname = ele[i].find_element(By.XPATH, "div/h4/a").text
    if productname == 'Blackberry':
        ele[i].find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//a[@class = 'nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 7)

wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
ele = driver.find_elements(By.XPATH, "//div[@class = 'suggestions']/ul/li/a")
for i in range(len(ele)):
    if ele[i].text == 'India':
        ele[i].click()
        break
driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@class = 'btn btn-success btn-lg']").click()
mes = driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']").text
print(mes)
assert "Success!" in mes