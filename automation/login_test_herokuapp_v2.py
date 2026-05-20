from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/login"


def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


def test_valid_login():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    driver.get(URL)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    success = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )

    assert "secure area" in success.text

    print("TC_001 PASS")
    driver.quit()


def test_invalid_password():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    driver.get(URL)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrongPassword123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash"))
    )

    assert "Your password is invalid!" in error.text

    print("TC_002 PASS")
    driver.quit()


def test_empty_username():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    driver.get(URL)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash"))
    )

    assert "Your username is invalid!" in error.text

    print("TC_003 PASS")
    driver.quit()


test_valid_login()
test_invalid_password()
test_empty_username()
