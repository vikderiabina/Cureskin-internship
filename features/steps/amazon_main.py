from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')



@given('Open amazon main page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_page()


@when('Search for {search_query}')
def search_amazon(context, search_query):
    context.app.header.search_amazon(search_query)


@when('click Orders')
def click_orders(context):
    context.app.header.click_orders()


@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.app.header.click_sign_in_popup_btn()


@when('Wait for {sec_amount} sec')
def wait_sec(context, sec_amount):
    sleep(int(sec_amount)) # sleep('5')


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Select department {text}')
def select_department(context, text):
    context.app.header.select_dept(text)


@then('Verify Sign In is clickable')
def verify_signin_popup_btn_clickable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable'
    )


@then('Verify Sign In disappears')
def verify_signin_popup_btn_disappears(context):
    context.driver.wait.until(  # .until_not
        EC.invisibility_of_element_located(POPUP_SIGNIN_BTN), # EC.visibility_of_element_located()
        message='Signin btn does not disappear'
    )


@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)

    links_count = len(context.driver.find_elements(*FOOTER_LINKS)) #36
    # print(context.driver.find_elements(*FOOTER_LINKS))
    # print(type(context.driver.find_elements(*FOOTER_LINKS)))
    assert links_count == expected_amount, f'Expected {expected_amount} links but got{links_count}'


@then('Verify Spanish option present')
def verify_spanish_lang_present(context):
    context.app.header.verify_spanish_lang_present()



