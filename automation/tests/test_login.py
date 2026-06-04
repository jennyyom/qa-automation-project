import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://the-internet.herokuapp.com/login"


# -----------------------------
# FIXTURE: setup / teardown
# -----------------------------
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # CI에서도 실행 가능하게 기본 안정 옵션
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver   # 테스트 실행 위치

    driver.quit()


# -----------------------------
# TC_001 - Valid Login
# -----------------------------
def test_valid_login(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(URL)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    success = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )

    assert "secure area" in success.text


# -----------------------------
# TC_002 - Invalid Login
# -----------------------------
def test_invalid_login(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(URL)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrongPassword")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash"))
    )

    assert "Your password is invalid!" in error.text


# -----------------------------
# TC_003 - Empty Username
# -----------------------------
def test_empty_username(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(URL)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash"))
    )

    assert "Your username is invalid!" in error.text