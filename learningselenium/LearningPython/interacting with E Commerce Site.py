from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get("http://localhost/opencart/upload/index.php?route=common/home&language=en-gb")
lap=driver.find_element(By.XPATH,'//a[starts-with(text(),"Laptops & Notebooks")]')
lap.click()
win=driver.find_element(By.XPATH,"//a[starts-with(text(),'Windows')]")
win.click()
search=driver.find_element(By.CSS_SELECTOR,"#search > input")
search.send_keys("Mac")
find=driver.find_element(By.CSS_SELECTOR,"#search > button")
find.click()
