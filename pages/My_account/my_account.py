"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import time

import allure
from datetime import datetime
from pages.base_page import BasePage
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException
)
from pages.My_account.my_account_locators import MyAccountLocator


class MyAccount(BasePage):

    @allure.step("Click 'Logout' button")
    def my_account_button_logout_click(self):
        print(f"\n"
              f"{datetime.now()}   Start Click [Logout] button:")

        print(f"{datetime.now()}   BUTTON_LOGOUT is present? =>")
        button_list = self.browser.find_elements(*MyAccountLocator.LOGOUT)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_LOGOUT is not present!")
            return False
        print(f"{datetime.now()}   => BUTTON_LOGOUT is present")
        print(f"{datetime.now()}   Is visible BUTTON_LOGOUT? =>")
        assert self.element_is_visible(MyAccountLocator.LOGOUT), "BUTTON_LOGOUT is not visible"
        print(f"{datetime.now()}   BUTTON_LOGOUT is clickable? =>")
        if not self.element_is_clickable(button_list[0], 10):
            print(f"{datetime.now()}   => BUTTON_LOGOUT is not clickable")
            return False

        print(f"{datetime.now()}   BUTTON_LOGOUT click =>")
        try:
            button_list[0].click()
        except ElementNotInteractableException:
            print(f'{datetime.now()}   It\'s problem! Button "Logout" is not clickable, but 1 second later ...')
            time.sleep(1)
            button_list[0].click()
        except ElementClickInterceptedException:
            print(f'{datetime.now()}   It\'s a problem! Button "Logout" are not clicked, but 1 second later ...')
            time.sleep(1)
            button_list[0].click()

        print(f"{datetime.now()}   => BUTTON_LOGOUT is clicked")

        return True

    @allure.step(f"{datetime.now()}.   Click 'Trading Platform' button")
    def click_button_trading_platform(self):
        button = self.browser.find_element(*MyAccountLocator.TRADING_PLATFORM)
        self.element_is_clickable(button, 5)
        button.click()

    @allure.step(f"{datetime.now()}.   Click 'Close MyAccount panel'")
    def click_close_user_panel(self):
        button = self.browser.find_element(*MyAccountLocator.CLOSE)
        self.element_is_clickable(button, 5)
        button.click()
