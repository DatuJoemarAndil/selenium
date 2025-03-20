import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get("https://www.facebook.com/")


driver.maximize_window()


wait = WebDriverWait(driver, 30)


time.sleep(15)
email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
email_input.send_keys("09318125600")


time.sleep(15)
password_input = wait.until(EC.presence_of_element_located((By.ID, "pass")))
password_input.send_keys( "marjoe")


time.sleep(15)
login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
login_button.click()


time.sleep(100)
driver.quit()