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

#XPATH="//tagname[@attribute='value']"

#By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-search-submit-button')

#By XPATH
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']")

#By XPATH, with quotes, exception
driver.find_element(By.XPATH, "//img[@alt=\'Dresses under $50\']")

#By XPATH, multiple attributes
driver.find_element(By.XPATH, "//input[@name='field-keywords' and @placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @name='field-keywords']")

#By XPATH, text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")

#By XPATH, text and attribute
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# HW2


#By XPATH, contains
driver.find_element(By.XPATH, "//a[contains(@href,'nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//a[contains(text(),'Best Sellers')]")
driver.find_element(By.XPATH, "//a[contains(text(),'Best Sellers') and @class='nav-a  ']")
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")

#By XPATH, from parent to child
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//div[@id='nav-xshop']//a[text()='Best Sellers']")

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



#__________________________________________________________________________________________________________________
#CSS selectors
#__________________________________________________________________________________________________________________




# By ID:
driver.find_element(By.ID, 'twotabsearchtextbox')

# Using ID in CSS:
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox') # tag can be removed

#Using ID and class:
driver.find_element(By.ID, '#twotabsearchtextbox.nav-input') # ID first, preffered
driver.find_element(By.ID, '.nav-input#twotabsearchtextbox')

# By CSS, using classes:
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag')
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-lop')
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-lop')

# By CSS, attributes:
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display"
                                     ".html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# By CSS, attributes, partial match: *=
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='ap_register_notification_privacy_notice']")


# Multiple attributes:
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-func-deps='aui-da-a-expander-toggle'][role='button']")
driver.find_element(By.CSS_SELECTOR, "[data-csa-c-func-deps='aui-da-a-expander-toggle'][role='button']") # no tag

# Multiple attributes + class:
driver.find_element(By.CSS_SELECTOR, "a.a-expander-header[data-csa-c-func-deps='aui-da-a-expander-toggle'][role='button']")

# By CSS, from parent to child:
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='condition']")
driver.find_element(By.CSS_SELECTOR, "div.a-section #legalTextRow a[href*='condition']")

# HW3

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










