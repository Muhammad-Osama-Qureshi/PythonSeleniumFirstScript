from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.support.wait import WebDriverWait

# from webdriver_manager.chrome import ChromeDriverManager#

driver = webdriver.Chrome()
driver.get("http://localhost/opencart/upload/index.php?route=account/login&language=en-gb")
elem = driver.find_element(By.LINK_TEXT, "Login")
elem.click()
email = driver.find_element(By.ID, "input-email")
email.send_keys("b@gmail.com")
passw = driver.find_element(By.ID, "input-password")
passw.send_keys("12345")
btn=driver.find_element(By.CSS_SELECTOR, "form button")
btn.click()

