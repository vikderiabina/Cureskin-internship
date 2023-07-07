from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage(Page):
    PRODUCT_NAME = (By.ID, 'productTitle')
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href*='/New-Arrivals']")
    WOMEN_LINK = (By.CSS_SELECTOR, "a[href*='/s?i=fashion-womens']")

    def get_product_name(self):
        return self.find_element(*self.PRODUCT_NAME).text

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_women_link(self):
        self.wait_for_element_appear(*self.WOMEN_LINK)
