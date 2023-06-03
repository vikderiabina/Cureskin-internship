from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
HEADER_LINKS = (By.CSS_SELECTOR, "#zg_header a")


@given('Open amazon BestSellers page')
def open_amazon_best_sellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify there are {expected_amount} links for BestSellers')
def verify_bestsellers_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    links_count = len(context.driver.find_elements(*HEADER_LINKS)) #5
    # print(context.driver.find_elements(*HEADER_LINKS))
    # print(type(context.driver.find_elements(*HEADER_LINKS)))
    assert links_count == expected_amount, f'Expected {expected_amount} links but got{links_count}'

