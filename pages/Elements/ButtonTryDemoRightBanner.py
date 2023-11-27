"""
-*- coding: utf-8 -*-
@Time    : 2023/05/31 22:00
@Author  : Liudmila Dankevich
"""

from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import RightBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class RightBannerTryDemo(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is visible BUTTON_CREATE_YOUR_ACCOUNT? =>")
        # if self.element_is_visible(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
        try:
            if self.browser.find_element(*RightBannerLocators.BUTTON_TRY_DEMO_RIGHT_BANNER):
                print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is visible on the page!")
        except NoSuchElementException:
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click '1. Create your account' button in 'Three first steps' section")
    def element_click(self):
        """Method"""
        print(f"\n{datetime.now()}   2. Act")
        button_list = self.browser.find_elements(*RightBannerLocators.BUTTON_TRY_DEMO_RIGHT_BANNER)
        if len(button_list) == 0:
            del button_list
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
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT NOT CLICKED")
            print("'Sign up' form or page is automatically opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            button_list[0].click()
            del page_

        del button_list
        return True
