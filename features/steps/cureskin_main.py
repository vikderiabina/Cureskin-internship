from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click Search')
def click_search(context):
    context.app.main_page.click_search()


@when('Search for {search_query}')
def search_cureskin(context, search_query):
    context.app.main_page.search_cureskin(search_query)
