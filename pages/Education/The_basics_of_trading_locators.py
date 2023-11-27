from selenium.webdriver.common.by import By


class TheBasicsOfTradingLocator:
    LOCATOR_THE_BASICS_OF_TRADING_TEXT = (By.CSS_SELECTOR, ".wrap>.cc-breadcrumbs")
    LOCATOR_BG_THE_BASICS_OF_TRADING_TEXT = (By.CSS_SELECTOR, "div.wrap>nav>span")
    LOCATOR_THE_BASICS_OF_TRADING_CREATE_VERIFY_YOUR_ACCOUNT_BUTTON = (By.CSS_SELECTOR,
                                                                       'div.regSteps__shape >'
                                                                       ' i.regSteps__item.js_signup')
