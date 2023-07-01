from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TOP_LINKS = (By.CSS_SELECTOR, "#zg_header a")
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/')
    context.driver.refresh()

@then('Verify there are {expected_amount} links for BestSellers')
def verify_bestsellers_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    links_count = len(context.driver.find_elements(*TOP_LINKS)) #5
    # print(context.driver.find_elements(*TOP_LINKS))
    # print(type(context.driver.find_elements(*TOP_LINKS)))
    assert links_count == expected_amount, f'Expected {expected_amount} links but got{links_count}'


@then('User can click through top links and verify correct page opens')
def click_thru_top_links(context):
    top_links = context.driver.find_elements(*TOP_LINKS)  # [WebEl1,WebEl2, WebEl3,... ]

    for i in range(len(top_links)):  # for i from 0 to 4 [0, 1, 2, 3, 4]
        link_to_click = context.driver.find_elements(*TOP_LINKS)[i] # 4
        link_text = link_to_click.text
        link_to_click.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'
