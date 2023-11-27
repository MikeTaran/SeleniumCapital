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
from pages.Elements.testing_elements_locators import ButtonFreeDemoOnHorizontalBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException


class ButtonFreeDemoOnHorizontalBanner(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            print(f"Current page is not {cur_item_link}")
            self.open_page()

        print(f"{datetime.now()}   Is present BUTTON_ON_HORIZONTAL_BANNER? =>")
        if self.element_is_visible(ButtonFreeDemoOnHorizontalBannerLocators.BUTTON_FREE_DEMO_ON_HOR_BANNER, 5):
            print(f"{datetime.now()}   => BUTTON_ON_HORIZONTAL_BANNER IS PRESENT")
        else:
            print(f"{datetime.now()}   => BUTTON_ON_HORIZONTAL_BANNER IS NOT PRESENT")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click button on horizontal banner")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        button_list = self.browser.find_elements(
            *ButtonFreeDemoOnHorizontalBannerLocators.BUTTON_FREE_DEMO_ON_HOR_BANNER)

        if len(button_list) == 0:
            del button_list
            return False

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
            print(f"{datetime.now()}   => ButtonOnHorBanner clicked")
        except ElementClickInterceptedException:
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
