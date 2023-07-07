from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'span.a-size-base-plus.a-color-base.a-text-normal')
PRODUCT_IMAGE = (By.CSS_SELECTOR, "[data-component-type='s-product-image']")


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results()


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(all_products)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Title cannot be blank'
        assert product.find_element(*PRODUCT_IMAGE).is_displayed, 'Image not found'


@then('Verify {text} department shown')
def verify_dept(context, text):
    context.app.search_results_page.verify_dept(text)



