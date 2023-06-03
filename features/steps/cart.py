
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, '#add-to-cart-button')
PRODUCT_PRICE = (By.CSS_SELECTOR, ".a-size-base.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
CART_ICON = (By.CSS_SELECTOR, '#nav-cart-count-container')
ONE_CART_ITEM = (By.CSS_SELECTOR, '#nav-cart-count')


@when('Click on the first search result')
def first_search_result(context):
    context.driver.find_element(*PRODUCT_PRICE).click()

@when('Click "Add to Cart" button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count-container').click()

@then('Verify cart has 1 item')
def check_cart(context):
    context.driver.find_element(*ONE_CART_ITEM).click()

