from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")
# create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
# input name field
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
# input email field
driver.find_element(By.CSS_SELECTOR, "#ap_email")
# input password field
driver.find_element(By.CSS_SELECTOR, "#ap_password")
# Passwords must be at least 6 characters
driver.find_element(By.XPATH, "//div[@class='a-alert-content'] [contains(text(),'Passwords must be')]")
# Re-enter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
# Create your Amazon account(Continue)
driver.find_element(By.CSS_SELECTOR, '#continue')
# Conditions of use
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_register_notification_condition_of_use')]")
# Privacy notice
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_register_notification_privacy_notice')]")
# Sign in
driver.find_element(By.CSS_SELECTOR, "a[href*='signin']")





