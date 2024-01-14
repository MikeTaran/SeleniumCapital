"""
-*- coding: utf-8 -*-
@Time    : 2023/05/26 00:40
@Author  : Alexander Tomelo
"""
# import time
# import os
# import sys
# import psutil
# import subprocess
# from memory_profiler import profile
# import random

import allure
import pytest

from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
# from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
# from pages.Elements.ButtonFreeDemoOnHorizontalBanner import ButtonFreeDemoOnHorizontalBanner
from src.src import CapitalComPageSrc


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    file_name = "tests/US_11_Education/US_11-02-04_Forex_trading/list_of_href.txt"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_02_04
class TestForexTradingItemPage:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.04", "Education > Menu item [Forex trading]",
            ".01_01", "Testing button [Start Trading] on Main banner")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "fr", "it", "cn", "ru"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.04", "Education > Menu item [Forex trading]",
            ".01_02", "Testing button [Try demo] on Main banner")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "fr", "it", "cn", "ru"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Start trading] in article")
    @pytest.mark.test_03
    def test_03_start_trading_button_in_content(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Start trading] in content
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.04", "Education > Menu item [Forex trading]",
            ".01_03", "Testing button [Start trading] in article")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "it"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Sell] in content block")
    @pytest.mark.test_04
    def test_04_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Sell] in content block
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.04", "Education > Menu item [Forex trading]",
            ".01_04", "Testing button [Sell] in content block")

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "it", "cn", "ru"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonContentBlock(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Buy] in content block")
    @pytest.mark.test_05
    def test_05_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Buy] in content block
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.04", "Education > Menu item [Forex trading]",
            ".01_05", "Testing button [Buy] in content block")

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "it", "cn", "ru"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonContentBlock(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.test_06
    def test_06_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.04", "Education > Menu item [Forex trading]",
            ".01_06", "Testing button [Trade] in Most traded block")

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "fr", "it", "cn", "ru"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button '1. Create your account' in 'Steps trading' block")
    @pytest.mark.test_07
    def test_07_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.04", "Education > Menu item [Forex trading]",
            ".01_07", "Testing button [1. Create your account] in block [Steps trading]")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "fr", "it", "cn", "ru"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Get started] on Sticky bar")
    @pytest.mark.test_08
    def test_08_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [1. Get started] on Sticky bar
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.04", "Education > Menu item [Forex trading]",
            ".01_08", "Testing button [Get started] on Sticky bar")

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "es", "it"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetStartedOnStickyBar(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

#
# class Tools:
#     @staticmethod
#     def clear_console():
#         if psutil.WINDOWS:
#             return os.system("cls")
#         else:
#             return os.system("clear")
#
#     @staticmethod
#     def check_output(command: str):
#         try:
#             return subprocess.check_output(command, shell=True,
#                                            universal_newlines=True,
#                                            stderr=subprocess.DEVNULL)
#
#         except subprocess.CalledProcessError:
#             return False
#
#
# def _swap():
#     used = round(psutil.swap_memory().used / 1e+6)
#     all_ = round(psutil.swap_memory().total / 1e+6)
#
#     return f'{used}MiB / {all_}MiB '
#
#
# def _storage():
#     all_ = round(psutil.disk_usage('/.').total / 1e+9)
#     used = round(psutil.disk_usage('/.').used / 1e+9)
#
#     return f'{used}GiB / {all_}GiB '
