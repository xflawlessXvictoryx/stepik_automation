from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_promo_url(self):
        assert "?promo=" in self.browser.current_url, "URL is not promo"

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        add_to_basket.click()

    def verify_added_product(self):
        self.verify_added_message()
        self.verify_basket_price()

    def verify_added_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_alert = self.browser.find_elements(*ProductPageLocators.ADDED_ALERT)[0].text
        assert product_name == added_alert, "Product name in alert is wrong"

    def verify_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price in basket_price, "Price is not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
