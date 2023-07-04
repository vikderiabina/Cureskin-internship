from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    CART_ICON = (By.CSS_SELECTOR, '#nav-cart-count-container')
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')

    def search_amazon(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_sign_in_popup_btn(self):
        self.wait_for_element_click(*self.POPUP_SIGNIN_BTN)

    def open_cart_page(self):
        self.click(*self.CART_ICON)