from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Set chrome options for working with headless mode (no screen)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

# Update webdriver instance of chrome-driver with adding chrome options
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
# driver = webdriver.Chrome("/Users/home/Desktop/chromedriver", options=chrome_options)
driver.implicitly_wait(30)


# Connect to the application
url = "http://ec2-3-234-241-135.compute-1.amazonaws.com:8080"
# url = "http://localhost:8080"

driver.get(url)
sleep(3)

vet_link = driver.find_element_by_link_text("VETERINARIANS")
vet_link.click()
sleep(5)

# Verify that table loaded
verify_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
sleep(3)

print("Table loaded")

driver.quit()