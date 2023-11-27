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
from pages.Elements.testing_elements_locators import VideoBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException


class VideoBanner(BasePage):
    """
    Video banner "Capital.com Try now
    Machen Sie Ihren ersten Handel mit capital.com
    Click on advertisment video
    """

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        # self.page_glossary = GlossaryPage(d, cur_item_link)

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        if not self.video_banner_is_visible():
            # pytest.fail("Checking element is not on this page")
            pytest.skip("Checking element is not on this page")

    @allure.step("Check if the element is present on the page")
    # @profile(precision=3)
    def video_banner_is_visible(self):
        print(f"{datetime.now()}   Is present VIDEO_BANNER? =>")
        if self.element_is_visible(VideoBannerLocators.VIDEO_BANNER):
            print(f"{datetime.now()}   => VIDEO_BANNER IS PRESENT")
            return True
        else:
            print(f"{datetime.now()}   => VIDEO_BANNER IS NOT PRESENT")
            return False

        # Act
    @allure.step("Click on video banner")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Is present VIDEO_BANNER? =>")
        button_list = self.browser.find_elements(*VideoBannerLocators.VIDEO_BANNER)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => VIDEO_BANNER not present")
            del button_list
            return False

        print(f"{datetime.now()}   => VIDEO_BANNER is present")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        print(f"{datetime.now()}   Is clickable VIDEO_BANNER? =>")
        if not self.element_is_clickable(button_list[0], 5):
            print(f"{datetime.now()}   => VIDEO_BANNER not clickable")
            del button_list
            return False

        try:
            print(f"{datetime.now()}   Click VIDEO_BANNER =>")
            button_list[0].click()
            print(f"{datetime.now()}   => VIDEO_BANNER CLICKED")
        except ElementClickInterceptedException:
            print("'Sign up'/'Log in' form or page is automatically opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            button_list[0].click()
            del page_

        del button_list
        return True
