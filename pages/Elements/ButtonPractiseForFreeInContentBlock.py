"""
-*- coding: utf-8 -*-
@Time    : 2023/06/22 13:30
@Author  : Andrey Bozhko
"""
from datetime import datetime
import pytest
import allure
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException
from pages.Elements.testing_elements_locators import ContentBlockLocators
from pages.Elements.AssertClass import AssertClass


class ButtonPractiseForFreeInContentBlock(BasePage):

    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        qty = self.arrange_v3(cur_item_link)

        for i in range(qty):
            self.element_click_v3(i)

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)

    def arrange_v3(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v3")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is visible BUTTON_PRACTISE_FOR_FREE? =>")

        print(f"{datetime.now()}   => BUTTON_PRACTISE_FOR_FREE? =>")
        buttons = self.browser.find_elements(*ContentBlockLocators.BUTTON_PRACTISE_FOR_FREE)
        if not buttons:
            pytest.skip("Checking element is not on this page")
            # print(f"{datetime.now()}   => BUTTON_PRACTISE_FOR_FREE? =>")
            # buttons = self.browser.find_elements(*ContentBlockLocators.BUTTON_PRACTISE_FOR_FREE2)
            # if not buttons:
            #     pytest.skip("Checking element is not on this page")
        return len(buttons)

    def arrange_(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is visible BUTTON_PRACTISE_FOR_FREE? =>")
        if self.element_is_visible(ContentBlockLocators.BUTTON_PRACTISE_FOR_FREE):
            print(f"{datetime.now()}   => BUTTON_PRACTISE_FOR_FREE is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_PRACTISE_FOR_FREE is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click 'Button Practise for free' in Content Block. V3")
    def element_click_v3(self, i):
        print(f"\n{datetime.now()}   2. Act_v3")
        print(f"{datetime.now()}   Start Click button BUTTON_PRACTISE_FOR_FREE_IN_ARTICLE =>")
        button_list = self.browser.find_elements(*ContentBlockLocators.BUTTON_PRACTISE_FOR_FREE)

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[int(i)]
        )
        if not self.element_is_clickable(button_list[int(i)], 5):
            print(f"{datetime.now()}   => BUTTON_PRACTISE_FOR_FREE_IN_ARTICLE is not clickable")
            pytest.fail("BUTTON_PRACTISE_FOR_FREE_IN_ARTICLE is not clickable")

        self.browser.execute_script("arguments[0].click();", button_list[int(i)])
        print(f"{datetime.now()}   => BUTTON_PRACTISE_FOR_FREE_IN_ARTICLE is clicked")

    @allure.step("Click 'Button Practise for free' in Content Block")
    def element_click(self):
        """Method"""
        print(f"\n{datetime.now()}   2. Act")
        button_list = self.browser.find_elements(*ContentBlockLocators.BUTTON_PRACTISE_FOR_FREE)
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
            print(f"{datetime.now()}   => BUTTON_PRACTISE_FOR_FREE IS CLICKED")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_PRACTISE_FOR_FREE IS NOT CLICKED")
        return True
