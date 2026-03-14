from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)


# web browser apne aap bnd nhi hoga.

driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(1)
# returns  the first occuring element and show error not found if id not found
name=driver.find_element(By.ID,"name")
phone_no=driver.find_element(By.ID,"phone")
nav_bar=driver.find_element(By.NAME,"Navbar")
# no such element: Unable to locate element:
# nav_bar=driver.find_element(By.NAME,"Nabar")
print(name)
print("name textfield found")
print(phone_no)
print("phone no textfield found")
print(nav_bar)
print("navigation bar found")
radio_button=driver.find_elements(By.CLASS_NAME,"form-check-input")

print(radio_button)
print(len(radio_button))
inp=driver.find_elements(By.TAG_NAME,"input")
print(len(inp))

# input[class="form-control"]


driver.quit()
