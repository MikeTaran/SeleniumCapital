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


class ButtonPractiseForFreeInContentBlock(BasePage):

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
