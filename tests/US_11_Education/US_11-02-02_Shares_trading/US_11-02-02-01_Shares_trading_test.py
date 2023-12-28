"""
-*- coding: utf-8 -*-
@Time    : 2023/11/03 00:40
@Author  : Mike Taran
"""
from datetime import datetime

import allure
import pytest

from pages.common import Common
from pages.conditions import Conditions
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
from pages.Elements.ButtonOnHorizontalBanner import ButtonOnHorizontalBanner
from pages.Elements.ButtonOnVerticalBanner import ButtonOnVerticalBanner
from src.src import CapitalComPageSrc


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    file_name = "tests/US_11_Education/US_11-02-02_Shares_trading/list_of_href.txt"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


def check_language(cur_language):
    if cur_language not in ["hu", "nl", "el"]:
        return
    pytest.skip(f"This test is not for {cur_language} language")


def check_country(cur_country):
    if cur_country in ["gb"]:
        pytest.skip(f"This test is not for {cur_country} country")


@pytest.mark.us_11_02_02
class TestSharesTradingItems:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Start Trading] on Main banner
        Language: All (Except: EL, HU, NL). License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.02", "Education > Menu item [Shares trading]",
            ".01_01", "Testing button [Start Trading] on Main banner")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.arrange_0()
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Try demo] on Main banner
        Language: All (Except: EL, HU, NL). License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.02", "Education > Menu item [Shares trading]",
            ".01_02", "Testing button [Try demo] on Main banner")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Sell] in content block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_03
    def test_03_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Sell] in content block
        Language: All (Except: EL, HU, NL, AR, ZH, CN). License: All (Except: FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.02", "Education > Menu item [Shares trading]",
            ".01_03", "Testing button [Sell] in content block")

        check_language(cur_language)
        if cur_language in ["ar", "zh", "cn"]:
            Common().skip_test_for_language(cur_language)
        check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonContentBlock(d, cur_item_link)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Buy] in content block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_04
    def test_04_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Buy] in content block
        Language: All (Except: EL, HU, NL, AR, ZH, CN). License: All (Except: FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.02", "Education > Menu item [Shares trading]",
            ".01_04", "Testing button [Buy] in content block")

        check_language(cur_language)
        if cur_language in ["ar", "zh", "cn"]:
            Common().skip_test_for_language(cur_language)
        check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonContentBlock(d, cur_item_link)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Start trading] in article")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_05
    def test_05_start_trading_button_in_content(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Start trading] in content
        Language: All (Except: EL, HU, NL). License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.02", "Education > Menu item [Shares trading]",
            ".01_05", "Testing button [Start trading] in article")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_06
    def test_06_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Trade] in Most traded block
        Language: All (Except: EL, HU, NL). License: All (Except: FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.02", "Education > Menu item [Shares trading]",
            ".01_06", "Testing button [Trade] in Most traded block")

        check_language(cur_language)
        check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Get started] on Sticky bar")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_07
    def test_07_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [1. Get started] on Sticky bar
        Language: All (Except: EL, HU, NL, AR, ZH, CN). License: All (Except: FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.02", "Education > Menu item [Shares trading]",
            ".01_07", "Testing button [Get started] on Sticky bar")

        check_language(cur_language)
        if cur_language in ["ar", "zh", "cn"]:
            Common().skip_test_for_language(cur_language)
        check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetStartedOnStickyBar(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button '1. Create your account' in 'Steps trading' block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_08
    def test_08_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All (Except: EL, HU, NL). License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.02", "Education > Menu item [Shares trading]",
            ".01_08", "Testing button [1. Create your account] in block [Steps trading]")

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button in block [Horizontal banner]")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_09
    def test_09_block_hor_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check the [Button] on the Horizontal banner at the bottom of the page.
        For "Authorized user" role:
        The trading platform page is opened depend on the banner [type-id]:
                Live mode if the banner in the Live mode banners list
                Demo mode if the banner in the Demo mode banners list
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.02", "Education > Menu item [Shares trading]",
            ".01_09", "Testing button in block [Horizontal banner]")

        check_language(cur_language)
        if cur_language in ["", "ar", "cn"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # банеры должны открываться в Demo mode for US_00
        banner00_hor_tpd = []
        # банеры должны открываться в Live mode for US_00
        banner00_hor_tp = []
        # банеры должны открываться в Demo mode for US_01
        banner01_hor_tpd = ['199', '294']
        # банеры должны открываться в Live mode for US_01
        banner01_hor_tp = ['169', '223', '254', '379', '392', '430', '429']

        test_element = ButtonOnHorizontalBanner(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link,
                                        banner00_hor_tpd, banner00_hor_tp, banner01_hor_tpd, banner01_hor_tp)

    @allure.step("Start test of button in block [Vertical banner]")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_10
    def test_10_block_vert_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
                Check the [Button] on the Vertical side banner at the bottom of the page.
                For "Authorized user" role:
                The trading platform page is opened depend on the banner [type-id]:
                        Live mode if the banner in the Live mode banners list
                        Demo mode if the banner in the Demo mode banners list
                """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.02", "Education > Menu item [Shares trading]",
            ".01_10", "Testing button in block [Vertical banner]")

        check_language(cur_language)
        if cur_language in ["", "ar", "cn"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # банеры должны открываться в Demo mode for US_00
        banner00_ver_tpd = []
        # банеры должны открываться в Live mode for US_00
        banner00_ver_tp = []
        # банеры должны открываться в Demo mode for US_01
        banner01_ver_tpd = ['251', '253', '380', '168', '222', '393']
        # банеры должны открываться в Live mode for US_01
        banner01_ver_tp = ['198', '293', '381', '391', '426']

        test_element = ButtonOnVerticalBanner(d, cur_item_link)
        test_element.full_test_with_tpi(
            d, cur_language, cur_country, cur_role, cur_item_link,
            banner00_ver_tpd, banner00_ver_tp, banner01_ver_tpd, banner01_ver_tp)
