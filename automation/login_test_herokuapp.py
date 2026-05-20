from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)

def go_to_login():
    driver.get("https://the-internet.herokuapp.com/login")

# TC_001 - Valid Login
def test_valid_login():
    go_to_login()
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    success = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
    print("TC_001 PASS:", success.text)

# TC_002 - Invalid Password
def test_invalid_password():
    go_to_login()
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrongPassword123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error = wait.until(EC.presence_of_element_located((By.ID, "flash")))
    print("TC_002 PASS:", error.text)

# TC_003 - Empty Username
def test_empty_username():
    go_to_login()
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error = wait.until(EC.presence_of_element_located((By.ID, "flash")))
    print("TC_003 PASS:", error.text)

# Run all tests
test_valid_login()
time.sleep(2)
test_invalid_password()
time.sleep(2)
test_empty_username()
time.sleep(2)

input("Press Enter to close browser...")
driver.quit()
