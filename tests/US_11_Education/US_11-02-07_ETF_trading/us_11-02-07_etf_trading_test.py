"""
-*- coding: utf-8 -*-
@Time    : 2023/07/28 18:15 GMT+3
@Author  : Aleksandr Tomelo
"""

import pytest
import allure
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Menu.menu import MenuSection


def check_language(cur_language, list_languages):
    if cur_language not in list_languages:
        pytest.skip(f"This test is not for '{cur_language}' language")


def check_country(cur_country, list_countries):
    if cur_country in list_countries:
        pytest.skip(f"This test is not for '{cur_country}' country")


@pytest.mark.us_11_02_07
class TestETFTrading:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All. Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.07", "Education > Menu item [ETF trading]",
            ".00_01", "Testing button [Start Trading] on Main banner")

        check_language(cur_language, ["", "ar", "de", "es", "it", "ru", "cn"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Try demo] on Main banner")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All. Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.07", "Education > Menu item [ETF trading]",
            ".00_02", "Testing button [Try demo] on Main banner")

        check_language(cur_language, ["", "ar", "de", "es", "it", "ru", "cn"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.test_03
    def test_03_most_traded_widget_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded widget
        Language: All. License: All. Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.07", "Education > Menu item [ETF trading]",
            ".00_03", "Testing button [Trade] in Most traded widget")

        check_country(cur_country, ["gb"])
        check_language(cur_language, ["", "ar", "de", "es", "it", "ru", "cn"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_menu_link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_menu_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    @pytest.mark.test_05
    def test_05_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.07", "Education > Menu item [ETF trading]",
            ".00_05",
            "Testing button [1. Create & verify your account] in block [Steps trading]")

        check_language(cur_language, ["", "ar", "de", "es", "it", "ru", "cn"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)
