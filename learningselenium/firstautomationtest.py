from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get("http://localhost/opencart/upload/index.php?route=account/login&language=en-gb")
elem = driver.find_element(By.LINK_TEXT, "Login")
elem.click()
email = driver.find_element(By.ID, "input-email")
email.send_keys("b@gmail.com")
passw = driver.find_element(By.ID, "input-password")
passw.send_keys("12345")
btn=driver.find_element(By.CSS_SELECTOR, "form button")
btn.click()
acc = driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(2)")
acc.click()
text=driver.find_element(By.XPATH, '//a[contains(text(),"Edit Account")]')
text.click()
name=driver.find_element(By.ID,'input-firstname')
name.clear()
name.send_keys("Muhammmad Osama")
lname=driver.find_element(By.ID,'input-lastname')
lname.clear()
lname.send_keys("Qureshi")
mail=driver.find_element(By.ID,"input-email")
mail.clear()
mail.send_keys('B@gmail.com')
con=driver.find_element(By.XPATH,"//button[@type='submit']")
con.click()

