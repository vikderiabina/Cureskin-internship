from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('a user is not logged in')
def is_user_not_logged_in(context):
    context.driver.get('https://www.amazon.com/')


@when('the user clicks on the Returns and Orders link')
def user_click_link(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()


@then('Verify Sign In page is present')
def is_sign_in_present(context):
    assert context.driver.find_element(By.XPATH, "//h1[@class = 'a-spacing-small']").is_displayed()
    sleep(2)


@then('Verify Sign email input field is present')
def email_input_field_is_present(context):
    assert context.driver.find_element(By.ID, "ap_email").is_displayed()
    sleep(2)

    context.driver.quit()

