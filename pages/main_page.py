from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SEARCH_BTN = (By.CSS_SELECTOR, "svg.icon.icon-search.modal__toggle-open")
    SEARCH_BTN_2 = (By.XPATH, "//button[@class='predictive-search__item--term button button--small button--full-width']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#Search-In-Modal")
    POP_UP_BTN = (By.XPATH, "//button[@class='popup-close']")

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')
        self.wait_for_element_click(*self.POP_UP_BTN)
        self.wait_for_element_disappear(*self.POP_UP_BTN)

    def click_search(self):
        self.wait_for_element_click(*self.SEARCH_BTN)

    def search_cureskin(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)
        self.wait_for_element_click(*self.SEARCH_BTN_2)

