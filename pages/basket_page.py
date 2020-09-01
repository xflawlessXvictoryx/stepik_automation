from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def verify_no_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def verify_empty_basket_text(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text
