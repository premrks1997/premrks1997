from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'D:\chromedriver_win32 (3)\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@placeholder = 'Search for Vegetables and Fruits']").send_keys("ber")
buttons = driver.find_elements(By.XPATH, "//div[@class = 'product-action']/button")
print(type(buttons))
for i in range(3):
    buttons[i].click()
list1 = driver.find_elements(By.XPATH, "//div[@class = 'product-action']/button/parent::div/parent::div/h4")
for i in range(3):
    print(list1[i].text)
driver.find_element(By.XPATH, "//a[@class = 'cart-icon']/img").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()
list2 = driver.find_elements(By.XPATH, "//td/p[@class = 'product-name']")
for i in range(3):
    print(list2[i].text)

assert list1 == list2