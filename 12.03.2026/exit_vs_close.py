from selenium import webdriver
opts=webdriver.ChromeOptions()
# using chrome
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.youtube.com")
driver.maximize_window()
# using edge browser
'''
opts=webdriver.EdgeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Edge(options=opts)
driver.get("https://www.youtube.com")
driver.maximize_window()'''
# driver.close() #closed the current window/tab
driver.quit()