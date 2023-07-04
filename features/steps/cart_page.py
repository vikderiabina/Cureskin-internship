
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, '#add-to-cart-button')
PRODUCT_PRICE = (By.CSS_SELECTOR, ".a-size-base.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
CART_ICON = (By.CSS_SELECTOR, '#nav-cart-count-container')
ONE_CART_ITEM = (By.CSS_SELECTOR, '#nav-cart-count')


@when('Click on the first search result')
def first_search_result(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Open cart page')
def open_cart_page(context):
    context.app.header.open_cart_page()

@then('Verify cart has {expected_item_count} item')
def check_cart(context, expected_item_count):
    expected_item_count = '1'
    actual_item_count = context.driver.find_element(*ONE_CART_ITEM).text
    assert expected_item_count == actual_item_count, f'Expected 1 item, but got {actual_item_count}'

@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name[:30] in actual_name, f'Expected {context.product_name} but got {actual_name}'



