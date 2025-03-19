import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box=driver.find_element(By.NAME, "q")
search_box.send_keys("SIMPLE SCRIPT PRACTICE")
time.sleep(5)
driver.quit()