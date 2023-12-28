"""
-*- coding: utf-8 -*-
@Time    : 2023/04/20 22:00
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure

from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import ElementClickInterceptedException


class BuyButtonContentBlock(BasePage):

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)

        # Checking if [SignUP for is popped up on the page]
        page_signup_login = SignupLogin(d, cur_item_link)
        page_signup_login.check_popup_signup_form()

        trade_instrument = self.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, False, True, trade_instrument)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_BUY_IN_CONTENT_BLOCK is located on the page? =>")
        button_list = self.elements_are_located(ButtonsOnPageLocators.BUTTON_TRADING_BUY, timeout=10)

        if not button_list:
            print(f"{datetime.now()}   => BUTTON_BUY_IN_CONTENT_BLOCK is not located on the page!")
            pytest.skip("ARRANGE: Checking element (BUTTON_BUY_IN_CONTENT_BLOCK) is not on this page")

        print(f"{datetime.now()}   => BUTTON_BUY_IN_CONTENT_BLOCK is located on the page!")

    @allure.step("Click button [Buy] in content block")
    def element_click(self, cur_role):
        print(f"\n{datetime.now()}   2. Act_v0")
        button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_TRADING_BUY)

        print(f"{datetime.now()}   BUTTON_BUY_IN_CONTENT_BLOCK is present? =>")
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_BUY_IN_CONTENT_BLOCK is not present on the page")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_BUY_IN_CONTENT_BLOCK is present on the page")

        print(f"{datetime.now()}   BUTTON_BUY_IN_CONTENT_BLOCK scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        print(f"{datetime.now()}   => BUTTON_BUY_IN_CONTENT_BLOCK scrolled")

        # Вытаскиваем линку из кнопки
        button_link = button_list[0].get_attribute('href')
        # Берём ID итема, на который кликаем для сравнения с открытым ID на платформе
        trade_instrument = button_link[button_link.find("spotlight") + 10:button_link.find("?")]

        print(f"{datetime.now()}   BUTTON_BUY_IN_CONTENT_BLOCK is clickable? =>")
        if not self.element_is_clickable(button_list[0], 5):
            print(f"{datetime.now()}   => BUTTON_BUY_IN_CONTENT_BLOCK is not clickable more then 5 sec.")
            pytest.fail("BUTTON_BUY_IN_CONTENT_BLOCK is not clickable more then 5 sec.")
        try:
            print(f"{datetime.now()}   BUTTON_BUY_IN_CONTENT_BLOCK CLICK =>")
            # button_list[0].click()
            self.browser.execute_script("arguments[0].click();", button_list[0])
            print(f"{datetime.now()}   => BUTTON_BUY_IN_CONTENT_BLOCK clicked!")

        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_BUY_IN_CONTENT_BLOCK NOT CLICKED")
            # сейчас бы сделать скриншот!

            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            # button_list[0].click()
            self.browser.execute_script("arguments[0].click();", button_list[0])
            del page_

        del button_list
        return trade_instrument
