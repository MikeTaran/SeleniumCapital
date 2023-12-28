"""
-*- coding: utf-8 -*-
@Time    : 2023/05/14 19:30 GMT+3
@Author  : Suleyman Alirzaev
"""
# import random
import pytest
import allure
# import sys
# from memory_profiler import profile
from datetime import datetime

from pages.common import Common
from pages.Elements.ButtonBuyInTable import BuyButtonTable
from pages.Elements.ButtonSellInTable import SellButtonTable
from test_data.cfd_markets import cfd_markets_href
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        file_name = "tests/US_11_Education/US_11-01-03_cfd_trading_guide/list_of_href.txt"
        list_item_link = Common().generate_cur_item_link_parameter(file_name)
        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


def check_cur_href(cur_item_link, list_href):
    if cur_item_link in list_href:
        return
    else:
        pytest.skip(f"This test case is not for page: '{cur_item_link}'")


@pytest.mark.us_11_01_03_01
class TestCFDTradingGuide:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        us = "11.01.03"
        tc = ".01_01"
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            us, "Education > Menu item [CFD trading guide]",
            tc, "Testing button [Start Trading] on Main banner")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "fr", "nl", "pl", "ro", "ru", "zh"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.03", "Education > Menu item [CFD trading guide]",
            ".01_02", "Testing button [Try demo] on Main banner")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "fr", "nl", "pl", "ro", "ru", "zh"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.test_03
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.03", "Education > Menu item [CFD trading guide]",
            ".01_03", "Testing button [Trade] in Most traded block")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "fr", "nl", "pl", "ro", "ru", "zh"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    @pytest.mark.test_04
    def test_04_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.03", "Education > Menu item [CFD trading guide]",
            ".01_04", "Testing button [Create your account] in block [Steps trading]")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "fr", "nl", "pl", "ro", "ru", "zh"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    # @allure.step('Start test "Click 2 from 5 random [Sell] buttons in "CFDs tables" for {type_fi} and {tab}')
    # def test_05_cfd_table_button_sell_tab(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         cur_type_fi, cur_tab):
    #     """
    #     Check: Button [1. Sell] in block "CFDs table" in {cur _tab} tab
    #     Language: All. License: All.
    #     """
    #     build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
    #                          "11.01.03", "Educations > Menu item [CFD trading guide]",
    #                          ".01_05", f"Testing 2 random buttons [Sell] in {cur_type_fi} table "
    #                                    f"and in {cur_tab} tab")
    #
    #     Common().check_language_in_list_and_skip_if_not_present(
    #         cur_language, ["", "de", "es", "nl", "pl", "ro", "ru", "zh"])
    #     check_cur_href(cur_item_link, cfd_markets_href)
    #
    #     page_conditions = Conditions(d, "")
    #     page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = SellButtonTable(d, cur_item_link)
    #     test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link, cur_type_fi, cur_tab)
    #
    # @allure.step('Start test "Click 2 from 5 random [Buy] buttons in CFDs tables" for {type_fi} and {tab}')
    # def test_06_cfd_table_button_buy_tab(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         cur_type_fi, cur_tab):
    #     """
    #     Check: Button [1. Buy] in block "CFDs table" in ... type_fi and ... tab
    #     Language: All. License: All.
    #     """
    #     build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
    #                          "11.01.03", "Educations > Menu item [CFD trading guide]",
    #                          ".01_06", f"Testing 2 button [Buy] in {cur_type_fi} table "
    #                                    f"and in {cur_tab} tab")
    #
    #     Common().check_language_in_list_and_skip_if_not_present(
    #         cur_language, ["", "de", "es", "nl", "pl", "ro", "ru", "zh"])
    #     check_cur_href(cur_item_link, cfd_markets_href)
    #
    #     page_conditions = Conditions(d, "")
    #     page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = BuyButtonTable(d, cur_item_link)
    #     test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link, cur_type_fi, cur_tab)
    #
    @allure.step("Start test of button [Start trading] in article")
    @pytest.mark.test_07
    def test_07_start_trading_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start trading] in article
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.03", "Education > Menu item [CFD trading guide]",
            ".01_07", "Testing button [Start trading] in article")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["de", "zh"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
