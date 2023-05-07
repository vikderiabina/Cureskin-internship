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

# driver.find_element(By.XPATH, 'nav-search-submit-button')


driver.find_element(By.ID, 'Amazon')  # Amazon logo
driver.find_element(By.ID, 'ap_email')  # Email field
driver.find_element(By.ID, 'continue')  # Continue button
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")  # Need help link
driver.find_element(By.ID, 'auth-fpp-link-bottom')  # Forgot your password link
driver.find_element(By.ID, 'ap-other-signin-issues-link')  # Other issues with Sign-In link
driver.find_element(By.ID, 'createAccountSubmit')  # Create your Amazon account button
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")  # Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")  # Privacy Notice link





