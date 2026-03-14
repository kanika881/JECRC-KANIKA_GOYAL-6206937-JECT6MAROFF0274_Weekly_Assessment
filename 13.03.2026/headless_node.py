from selenium import webdriver
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
# background m chalega browser
opts.add_argument('--headless')

# web browser apne aap bnd nhi hoga.

driver = webdriver.Chrome(options=opts)
driver.get("https://supertails.com/")
driver.maximize_window()


# driver.close()
# close a single window

driver.quit()
#  closes all the window  and cut connection