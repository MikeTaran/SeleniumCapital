"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 19:00 GMT+3
@Author  : Suleyman Alirzaev
"""
import pytest
import allure

from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonsSellBuyInContentBlock import ButtonsSellBuyInContentBlock
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.ButtonSignupLoginOnPage import PageSignUpLogin
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators

count = 1


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    file_name = "tests/US_11_Education/US_11-02-05_Cryptocurrency_trading/list_of_href.txt"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_02_05
class TestCryptocurrencyTrading:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    @pytest.mark.test_03
    def test_03_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_03", "Testing button [Start Trading] on Main banner")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = MainBannerStartTrading(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Try demo] on Main banner")
    @pytest.mark.test_04
    def test_04_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_04", "Testing button [Try demo] on Main banner")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = MainBannerTryDemo(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.test_05
    def test_05_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_05", "Testing button [Trade] in Most traded block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # times = 5
        most_traded_quantity = d.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
        if cur_country != 'gb':
            for i in range(len(most_traded_quantity)):
                test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
                test_element.arrange_v3(d, cur_item_link)

                test_element.element_click_v3(i, cur_role)

                test_element = AssertClass(d, cur_item_link)
                match cur_role:
                    case "NoReg":
                        test_element.assert_signup(d, cur_language, cur_item_link)
                    case "NoAuth":
                        test_element.assert_login(d, cur_language, cur_item_link)
                    case "Auth":
                        test_element.assert_trading_platform_v4(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Start trading] in article")
    @pytest.mark.test_06
    def test_06_start_trading_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start trading] in article
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_06", "Testing button [Start trading] in article")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = ContentStartTrading(d, cur_item_link)
            test_element.arrange_(cur_item_link)

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of buttons [Sign up] on page")
    @pytest.mark.test_07
    def test_07_sign_up_on_page_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Buttons [Sign up] on page
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_07", "Testing buttons [Sign up] on page")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = PageSignUpLogin(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    @pytest.mark.test_08
    def test_08_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_08", "Testing button [Create your account] in block [Steps trading]")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = BlockStepTrading(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg" | "NoAuth":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Sell] in content block")
    @pytest.mark.test_09
    def test_09_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [1. Sell] in content block
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_09", "Testing button [Sell] in content block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = ButtonsSellBuyInContentBlock(d, cur_item_link)
            test_element.arrange_(cur_item_link, button='sell')

            test_element.element_click(cur_role)

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Buy] in content block")
    @pytest.mark.test_10
    def test_10_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [1. Buy] in content block
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_10", "Testing button [Sell] in content block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = ButtonsSellBuyInContentBlock(d, cur_item_link)
            test_element.arrange_(cur_item_link, button='buy')

            test_element.element_click(cur_role)

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Get started] on Sticky bar")
    @pytest.mark.test_11
    def test_11_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [1. Get started] on Sticky bar
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_11", "Testing button [Get started] on Sticky bar")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = GetStartedOnStickyBar(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")
