#there is certain syntax to write in xpath xml path
# use @attribute
# use / absolute xpath  eg /html/body/div/input[@id="name"]
#  use // relative xpath we use relative path eg // input[@id="name"] if there are two do (input[@id="name"])[1]
# //input[@placeholder="Enter Name"]
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
main=driver.find_element(By.XPATH,'//div[@name="Main"]')
days=driver.find_element(By.XPATH,'//label[@for="days"]')
# inner text using //a[text()=]
s = driver.find_element(By.XPATH,'//a[text()="Home"]')
s.click()
p=driver.find_element(By.XPATH,'//button[text()="START"]')
print(p)
# we will
'''
l=driver.find_elements(By.XPATH,'//h1[text()=" Automation Testing practice"]')
print(l)

k=driver.find_elements(By.XPATH,'//option[text()]="United States"]')
print(k)


'''
#  we will be using conatins in above to solve the error
c=driver.find_elements(By.XPATH,'//option[contains (text(),"United")]')
print(c)
driver.maximize_window()
driver.quit()