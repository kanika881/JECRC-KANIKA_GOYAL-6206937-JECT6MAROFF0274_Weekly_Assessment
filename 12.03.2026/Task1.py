from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://topbrains.com/")

driver.maximize_window()
sleep(4)
#using sleep
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(3)
driver.minimize_window()
sleep(4)
driver.close()


print(f"Driver Name:{driver.name}")
print(f"Driver URL:{driver.current_url}")
print(f"Driver Title:{driver.title}")
# opts=webdriver.Chromeoptions()
# opts.add_argumental_option("detach",True)
# driver=webdriver.Chrome(options=opts)
# driver.get("https://topbrains.com/")


