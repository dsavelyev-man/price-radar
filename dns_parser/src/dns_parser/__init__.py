from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Requires ChromeDriver
driver.get('https://www.dns-shop.ru/catalog')
elements = driver.find_elements(By.TAG_NAME, 'div')
for elem in elements:
    print(elem.text)
driver.quit()
