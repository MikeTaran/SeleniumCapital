"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 19:45
@Author  : Alexander Tomelo
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonInBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException


class ButtonInBanner(BasePage):

    @allure.step("Check that the element is present on the page")
    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            print(f"Current page is not {cur_item_link}")
            self.open_page()

        print(f"{datetime.now()}   BUTTON_IN_BANNER =>")
        if self.element_is_visible(ButtonInBannerLocators.BUTTON_IN_BANNER):
            print(f"{datetime.now()}   => BUTTON_IN_BANNER IS PRESENT")
            # return True
        else:
            print(f"{datetime.now()}   => BUTTON_IN_BANNER IS NOT PRESENT")
            pytest.skip("Checking element is not on this page")
            # return False

    @allure.step("Click button on inBanner")
    def element_click(self):
        """Method"""
        print(f"\n{datetime.now()}   2. Act")
        button_list = self.browser.find_elements(*ButtonInBannerLocators.BUTTON_IN_BANNER)

        if len(button_list) == 0:
            del button_list
            return False

        print(f"{datetime.now()}   "
              f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_IN_BANNER CLICKED")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_IN_BANNER NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button_list[0]
            )
            self.element_is_clickable(button_list[0], 5)

            button_list[0].click()
            del page_

        del button_list
        return True
