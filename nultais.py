import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time

try:
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)
    url = "https://www.y8.com"
    driver.get(url)
    time.sleep(3)

    find=driver.find_element(By.ID," css-ik5ir8")
    print(find)

except Exception as e:
    print(f"Error: {e}")
