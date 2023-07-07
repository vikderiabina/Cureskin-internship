from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    BOOKS_SUBMENU = (By.XPATH, "//div[@id='nav-subnav'] /a[1]")


    def verify_search_results(self, expected_result):
        actual_result = self.driver.find_element(*self.RESULT_TEXT).text
        assert expected_result == actual_result, f"Error! Expected {expected_result} but got actual {actual_result}"

    def verify_dept(self, texts):
        self.wait_for_element_appear(*self.BOOKS_SUBMENU)
        expected_text = texts
        actual_text = self.driver.find_element(*self.BOOKS_SUBMENU).text
        assert expected_text.upper() == actual_text.upper(), f"Doesnt match"



