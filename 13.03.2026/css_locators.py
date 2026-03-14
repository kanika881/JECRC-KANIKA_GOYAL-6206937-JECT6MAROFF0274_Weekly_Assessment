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
#"class . id #""
name1=driver.find_element(By.CSS_SELECTOR,"select[id='animals']")
name2=driver.find_element(By.CSS_SELECTOR,"#animals")
print(name1)
print(name2)
# * means giving partial symbol
# <a href="http://testautomationpractice.blogspot.com/">Home</a>
# a[href*="testautomationpractice"]
anchor=driver.find_element(By.CSS_SELECTOR,'a[href*="testautomationpractice"]')
print("a",anchor)
# (^)my elements starts with
anchor1=driver.find_element(By.CSS_SELECTOR,'a[href^="http://"]')
print("a",anchor1)
# $ for elemets ending and it only find first occurence
anchor2=driver.find_element(By.CSS_SELECTOR,'a[href$="com/"]')
print(f"using $:",anchor2)

# css selector
# tagname[attribute=value]
# disadvantage of using css selector you cant find inner tags and you cant tarverse downwards
# combine two attributes
# input[type="text"][class="classname"]
# combining two css selectors
# div ul li  a[href*="testautomation"]
# div[class="widget-content"] a[href*="testautomation"]
