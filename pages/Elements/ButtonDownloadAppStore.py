"""
-*- coding: utf-8 -*-
@Time    : 2023/06/20 09:30
@Author  : Andrey Bozhko
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException
from pages.Elements.testing_elements_locators import BlockSignUpAndTradeSmartTodayLocators


class ButtonDownloadAppStore(BasePage):

    def arrange_(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is visible BUTTON_DOWNLOAD_APP_STORE? =>")
        if self.element_is_visible(BlockSignUpAndTradeSmartTodayLocators.BUTTON_DOWNLOAD_APP_STORE):
            print(f"{datetime.now()}   => BUTTON_DOWNLOAD_APP_STORE is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_DOWNLOAD_APP_STORE is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click 'Button Download on the App Store' in Block 'Sign up and trade smart today!'")
    def element_click(self):
        """Method"""
        print(f"\n{datetime.now()}   2. Act")
        button_list = self.browser.find_elements(*BlockSignUpAndTradeSmartTodayLocators.BUTTON_DOWNLOAD_APP_STORE)
        if len(button_list) == 0:
            return False
        print(f"{datetime.now()}   "
              f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        self.element_is_clickable(button_list[0], 10)
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_DOWNLOAD_APP_STORE IS CLICKED")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_DOWNLOAD_APP_STORE IS NOT CLICKED")
        return True
