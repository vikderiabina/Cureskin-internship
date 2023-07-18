from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT_TEXT = (By.CSS_SELECTOR, "#ProductCount")

    def verify_search_results(self, expected_result):
        actual_result = self.driver.find_element(*self.RESULT_TEXT).text
        assert expected_result in actual_result,  f"Error! Expected {expected_result} but got actual {actual_result}"




