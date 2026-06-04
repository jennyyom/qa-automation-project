from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium. webdriver. support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# QA approach: waiting for conditions
wait = WebDriverWait(driver, 10)

search_box = wait.until(
    EC.presence_of_element_located((By.NAME, "q"))
)

search_box.send_keys("Selenium QA automation")

search_box.send_keys(Keys.RETURN)

time.sleep(3)

input("Press Enter to close browser...")
driver.quit()
