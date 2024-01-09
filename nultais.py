from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver  = webdriver.Edge(executable_path=r"C:\Windows\msedgedriver.exe")

URL = "https://www.y8.com"
driver.get(URL)

wait = WebDriverWait(driver, 5)
agree = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-ik5ir8")))
agree.click()
got_it = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "validate-policy")))
got_it.click()
search = wait.until(EC.element_to_be_clickable((By.ID, "q")))
search.send_keys("Sinjid")
findgame = wait.until(EC.element_to_be_clickable((By.ID, "ui-id-2")))
findgame.click()
download_game = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "download-link")))
download_game.click()
time.sleep(20)

driver.quit()
