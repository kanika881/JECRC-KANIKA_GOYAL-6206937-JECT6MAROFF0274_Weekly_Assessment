from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.youtube.com")
driver.maximize_window()
# driver.close()
driver.quit()
# driver.