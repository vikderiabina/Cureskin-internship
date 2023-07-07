from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Header(Page):
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    CART_ICON = (By.CSS_SELECTOR, '#nav-cart-count-container')
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    ORDERS_BTN = (By.ID, 'nav-orders')
    LANG_OPTIONS = (By.CSS_SELECTOR, '#icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPT_SELECT = (By.ID, 'searchDropdownBox')
    BOOK = 'search-alias=stripbooks'
    APPLIANCES = 'search-alias=appliances'

    def search_amazon(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_sign_in_popup_btn(self):
        self.wait_for_element_click(*self.POPUP_SIGNIN_BTN)

    def open_cart_page(self):
        self.click(*self.CART_ICON)

    def hover_lang(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)

        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()
        sleep(3)

    def select_dept(self, word):
        dept_select = self.find_element(*self.DEPT_SELECT)
        select = Select(dept_select)
        if word == "books":
            select.select_by_value(self.BOOK)
        else:
            select.select_by_value(self.APPLIANCES)

    def verify_spanish_lang_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)
