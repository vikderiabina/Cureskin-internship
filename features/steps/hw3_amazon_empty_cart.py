from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on "Cart" icon')
def click_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '.nav-cart-icon').click()

@then('Verify that Amazon Cart has the following text {expected_result}')
def cart_empty(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual{actual_result}'

    context.driver.quit()

print('Test passed!')