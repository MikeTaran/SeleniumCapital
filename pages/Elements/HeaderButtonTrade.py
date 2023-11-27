"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 08:30
@Author  : Alexander Tomelo
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import HeaderButtonTradeLocators
from selenium.common.exceptions import ElementClickInterceptedException


class HeaderButtonTrade(BasePage):

    def arrange_(self, d, cur_role, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if cur_role == "Auth":
            pytest.skip('This test not for "Auth" role')

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_SIGNUP is visible? =>")
        if self.element_is_visible(HeaderButtonTradeLocators.BUTTON_TRADE):
            print(f"{datetime.now()}   => BUTTON_SIGNUP is visible on the page!")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_SIGNUP is not visible on the page!")
            pytest.skip("Checking element is not present on this page")

    @allure.step("Click button [Trade Now]")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   BUTTON_SIGNUP is present? =>")
        button_list = self.browser.find_elements(*HeaderButtonTradeLocators.BUTTON_TRADE)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_SIGNUP is not present on the page!")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_SIGNUP is present on the page!")

        print(f"{datetime.now()}   BUTTON_SIGNUP scroll =>")

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_SIGNUP clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_SIGNUP NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            button_list[0].click()
            del page_

        del button_list
        return True
