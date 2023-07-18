from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    context.app.search_results.verify_search_results(expected_result)
