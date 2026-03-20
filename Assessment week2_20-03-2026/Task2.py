
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

wait = WebDriverWait(driver, 15)

driver.get("https://automationexercise.com/signup")
driver.maximize_window()
username=wait.until(EC.presence_of_element_located((By.XPATH,'//form[@action="/signup"]/child::input[@placeholder="Name"]')))
username.click()
username.send_keys("kanika goyal")
email=wait.until(EC.presence_of_element_located((By.XPATH,'//form[@action="/signup"]/child::input[@placeholder="Email Address"]')))
email.click()
email.send_keys("kanika123@gmail.com")
btn=wait.until(EC.element_to_be_clickable((By.XPATH,'//form[@action="/signup"]/child::button[@type="submit"]')))
btn.click()

# driver.get("https://automationexercise.com/signup")
gender=wait.until(EC.element_to_be_clickable((By.ID,'id_gender2')))
gender.click()
newsletter=wait.until((EC.element_to_be_clickable((By.ID,'newsletter'))))
newsletter.click()
offers=wait.until(EC.element_to_be_clickable((By.ID,"optin")))
offers.click()

print("Newsletter selected:", newsletter.get_attribute("checked"))


print("Special offers selected:", offers.get_attribute("checked"))