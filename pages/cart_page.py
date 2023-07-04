from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')

    def verify_cart_is_empty(self):
        self.verify_element_text('Your Amazon Cart is empty', *self.EMPTY_CART)