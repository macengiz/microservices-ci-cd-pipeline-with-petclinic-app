from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


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
owners_link = driver.find_element_by_link_text("OWNERS")
owners_link.click()
sleep(2)

all_link = driver.find_element_by_link_text("REGISTER")
all_link.click()
sleep(2)

# Register new Owner to Petclinic App
fn_field = driver.find_element_by_name('firstName')
fn = 'Callahan' + str(random.randint(0, 100))
fn_field.send_keys(fn)
sleep(1)

fn_field = driver.find_element_by_name('lastName')
fn_field.send_keys('Clarusway')
sleep(1)

fn_field = driver.find_element_by_name('address')
fn_field.send_keys('Ridge Corp. Street')
sleep(1)

fn_field = driver.find_element_by_name('city')
fn_field.send_keys('McLean')
sleep(1)

fn_field = driver.find_element_by_name('telephone')
fn_field.send_keys('+1230576803')
sleep(1)

fn_field.send_keys(Keys.ENTER)
sleep(10)

# Wait until Owner List table loaded
verify_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
# Verify that new user is added to Owner List
if fn in driver.page_source:
    print(fn, 'is added and found in the Owners Table')
    print("Test Passed")
else:
    print(fn, 'is not found in the Owners Table')
    print("Test Failed")

driver.quit()