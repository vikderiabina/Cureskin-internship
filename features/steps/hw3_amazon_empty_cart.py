
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@then('Verify that Amazon Cart has the following text {expected_result}')
def verify_cart_is_empty(context, expected_result):
    context.app.cart_page.verify_cart_is_empty()


