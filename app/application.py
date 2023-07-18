from pages.main_page import MainPage
from pages.search_results import SearchResultsPage
# from pages.sign_in_page import SignInPage
# from pages.header import Header
# from pages.cart_page import CartPage
# from pages.product_page import ProductPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results = SearchResultsPage(self.driver)

        # self.header = Header(self.driver)

        # self.sign_in_page = SignInPage(self.driver)
        # self.cart_page = CartPage(self.driver)
        # self.product_page = ProductPage(self.driver)
