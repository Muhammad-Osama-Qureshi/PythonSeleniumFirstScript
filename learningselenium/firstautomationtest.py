from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options)
# driver.get('http://google.com/')
#
# #options = webdriver.ChromeOptions()
# #options.add_experimental_option("detach", True)
# options = webdriver.FirefoxOptions()
# # options.add_experimental_option("detach", True)
# driver=webdriver.Firefox()


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
# time.sleep(8)
driver.maximize_window()
# driver.execute_script("window.scrollTo(0,4000)","")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

driver.find_element(By.XPATH,"//div[@class='list-group mb-3']/a[contains(text(),'Log')]").click()
driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div/a").click()


lap=driver.find_element(By.XPATH,'//a[starts-with(text(),"Laptops & Notebooks")]')
lap.click()
win=driver.find_element(By.XPATH,"//a[starts-with(text(),'Windows')]")
win.click()
search=driver.find_element(By.CSS_SELECTOR,"#search > input")
search.send_keys("Mac")
find=driver.find_element(By.CSS_SELECTOR,"#search > button")
find.click()
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
Mac=driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[5]/div[2]/form/div/div[1]/a/img")
Mac.click()
atc=driver.find_element(By.XPATH,"//*[@id='button-cart']")
atc.click()
item=driver.find_element(By.XPATH,"/html/body/header/div/div/div[3]/div/button")
item.click()
checkout=driver.find_element(By.XPATH,"/html/body/header/div/div/div[3]/div/ul/li/div/p/a[2]/strong/i")
checkout.click()

# print(log)
# try:
#     log.click()
# except :
#     print("e")


