import allure
import datetime
from pages.base_page import BasePage
from pages.Education.The_basics_of_trading_locators import TheBasicsOfTradingLocator


class TheBasicsOfTrading(BasePage):
    # Проверка текущего URL
    @allure.step(f"{datetime.datetime.now()}. Current_url.")
    def tc_01_01_current_url(self):
        current_url = self.browser.current_url
        check_current_url = "https://capital.com/basics-of-trading"
        assert current_url == check_current_url, f'Text on UI {current_url} is not eq {check_current_url}'

    # Проверка наличия текста на странице
    @allure.step(f"{datetime.datetime.now()}. Should_be_The_basics_of_trading_text.")
    def tc_should_be_the_basics_of_trading_text(self):
        if self.element_is_present(*TheBasicsOfTradingLocator.LOCATOR_THE_BASICS_OF_TRADING_TEXT):
            basics_of_trading = self.browser.find_element(*TheBasicsOfTradingLocator.LOCATOR_THE_BASICS_OF_TRADING_TEXT)
            basics_of_trading_text = basics_of_trading.text
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                basics_of_trading)
            check_text = "The basics of trading"
            assert basics_of_trading_text == check_text, f'Text on UI {basics_of_trading_text} is not eq {check_text}'
            return True
        else:
            return False

    @allure.step(F"{datetime.datetime.now()}.Click '1.Create verify your account' button in "
                 F"'Three first steps' section")
    def tc_01_01_click_button_1_create_verify_your_account_button(self):
        if self.element_is_present(
                *TheBasicsOfTradingLocator.LOCATOR_THE_BASICS_OF_TRADING_CREATE_VERIFY_YOUR_ACCOUNT_BUTTON
        ):
            button = self.browser.find_element(*TheBasicsOfTradingLocator.
                                               LOCATOR_THE_BASICS_OF_TRADING_CREATE_VERIFY_YOUR_ACCOUNT_BUTTON)
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button)
            self.element_is_clickable(button, 5)
            button.click()
            return True
        else:
            return False
