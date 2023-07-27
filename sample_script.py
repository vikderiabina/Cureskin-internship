from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\vderiabina\PycharmProjects\Cureskin-internship\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Applied to all Find Element functions
# 100 ms = 0.1 s
# Defined once
# Not modifying the Error / Exception
driver.implicitly_wait(5)

# start with driver.wait
# checks the condition to be met every 500 ms (1/2 s)
# defined in the spot where we need it
# always fails with TimeoutException
driver.wait = WebDriverWait(driver, 5)


# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Car')
# driver.implicitly_wait(0)
# driver.implicitly_wait(5)

# wait for 4 sec
# sleep(4)
google_search_btn = (By.NAME, 'btnK')
driver.wait.until(EC.element_to_be_clickable(google_search_btn), message='Google search btn not clickable')

# click search button
driver.find_element(*google_search_btn).click()

# verify search results
assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
