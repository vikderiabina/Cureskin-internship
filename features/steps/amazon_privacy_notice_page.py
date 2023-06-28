from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_LINK = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_amazon_terms_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original:', context.original_window)
    print('All windows:', context.driver.window_handles)


@when('Click on Amazon Privacy Notice link')
def click_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer'))

