from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep




# Open Amazon
# Verify page title and current URL
# Locate the category dropdown (next to search bar)
# Select "Books" using Select class
# Enter "Harry Potter" in search and press Enter
# Use explicit wait to wait until results are visible
# Get all product titles using find_elements
# Print first 5 product names
# Click on the first product


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

wait = WebDriverWait(driver, 15)

driver.get("https://www.amazon.in")
driver.maximize_window()
# Verify page title and current URL

print("The title of the page is :",driver.title)

print("The URL of the page is :",driver.current_url)
assert "https://www.amazon.in/" == driver.current_url,"URL not verfied"
print("URL verified successfully")


dropdown = wait.until(EC.presence_of_element_located((By.ID, "searchDropdownBox")))
sleep(2)
select = Select(dropdown)
select.select_by_visible_text("Books")
searchbar=wait.until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox")))
searchbar.send_keys("Harry Potter")
btn=wait.until(EC.element_to_be_clickable((By.ID,"nav-search-submit-button")))
btn.click()
wait.until(EC.presence_of_all_elements_located((By.ID,"search")))
# //h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]
books=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]')))
for i in range(0,6):

    print(books[i].text)
first=wait.until(EC.presence_of_element_located((By.XPATH,'(//div[@class="a-section aok-relative s-image-fixed-height"])[1]/img')))
first.click()
driver.quit()





