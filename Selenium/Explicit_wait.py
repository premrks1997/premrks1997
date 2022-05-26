from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service(r'D:\chromedriver_win32 (3)\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("c")

driver.maximize_window()
driver.find_element(By.XPATH, "//input[@placeholder = 'Search for Vegetables and Fruits']").send_keys("ber")
elements = driver.find_elements(By.XPATH, "//div[@class = 'product']")
count = len(elements)
assert count == 3
buttons = driver.find_elements(By.XPATH, "//div[@class = 'product-action']/button")
buttons[1].click()
buttons[2].click()
driver.find_element(By.XPATH, "//a[@class = 'cart-icon']/img").click()
driver.find_element(By.XPATH, "//button[text() ='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
print(driver.find_element(By.XPATH, "//span[@class = 'promoInfo']").text)