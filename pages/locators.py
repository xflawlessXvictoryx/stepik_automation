from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.CSS_SELECTOR, ".basket-mini .btn-group")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD_FORM = (By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRM_PASSWORD_FORM = (By.CSS_SELECTOR, "[name='registration-password2']")
    SUBMIT_REGISTER = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADDED_ALERT = (By.CSS_SELECTOR, "#messages .alertinner  strong")
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner ")


class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
