from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    add_to_cart_btn = context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN),
        message='Add to cart btn not clickable')
    add_to_cart_btn.click()


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@then('Verify user can click through {colors}')
def verify_can_click_colors(context, colors):
    expected_colors = colors.split(',,')
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # => [WebElement1, WebElement2, WebElement3]

    for color in colors[:6]:
        # WebElement1
        color.click()  # WebElement1.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors.append(current_color)

    assert expected_colors == actual_colors, \
        f'Expected colors{expected_colors} did not match actual {actual_colors}'


