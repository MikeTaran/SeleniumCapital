"""
-*- coding: utf-8 -*-
@Time    : 2023/04/20 22:00
@Author  : Suleyman Alirzaev
"""
from datetime import datetime

import pytest
import allure
from selenium.common.exceptions import ElementClickInterceptedException

from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from pages.Elements.AssertClass import AssertClass


class ArticleCreateAccount(BasePage):

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):

        self.arrange_(d, cur_item_link)

        self.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_CREATE_ACCOUNT is visible? =>")
        # if self.element_is_visible(ButtonsOnPageLocators.BUTTON_CREATE_ACCOUNT):
        if self.element_is_visible(ButtonsOnPageLocators.BUTTON_CREATE_ACCOUNT, 5):
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click button [Create account] in article")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   BUTTON_CREATE_ACCOUNT is present? =>")
        button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_CREATE_ACCOUNT)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT is not present on the page!")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT is present on the page!")

        print(f"{datetime.now()}   BUTTON_CREATE_ACCOUNT scroll =>")

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT NOT CLICKED")
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
