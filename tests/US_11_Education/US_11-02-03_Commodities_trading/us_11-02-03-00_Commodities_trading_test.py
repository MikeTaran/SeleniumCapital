"""
-*- coding: utf-8 -*-
@Time    : 2023/04/19 17:00 GMT+3
@Author  : Suleyman Alirzaev
"""
# import os.path
import pytest
import allure
from datetime import datetime

from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonOnHorizontalBanner import ButtonOnHorizontalBanner
from pages.Elements.ButtonOnVerticalBanner import ButtonOnVerticalBanner
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.common import Common
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.testing_elements_locators import SubPages

count = 1


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


def check_language(cur_language):
    if cur_language in ["hu", "nl", "el"]:
        pytest.skip(f"This test is not for {cur_language} language")


def check_country(cur_country):
    if cur_country in ["gb"]:
        pytest.skip(f"This test is not for {cur_country} country")


@pytest.mark.us_11_02_03
# @allure.epic('US_11.02.03 | Find materials pages in "Commodities trading" menu')
class TestCommoditiesTradingPretest:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] on Main banner
        Language: All (Except: EL, HU, NL). License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.03", "Education > Menu item [Commodities trading]",
            ".00_01", "Testing button [Start Trading] on Main banner")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.arrange_0()
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_commodities_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = MainBannerStartTrading(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on Main banner
        Language: All (Except: EL, HU, NL). License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.03", "Education > Menu item [Commodities trading]",
            ".00_02", "Testing button [Try demo] on Main banner")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_commodities_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = MainBannerTryDemo(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Start test of buttons [Trade] in Most traded widget")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_06
    def test_06_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded block
        Language: All (Except: EL, HU, NL). License: All (Except: FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.03", "Education > Menu item [Commodities trading]",
            ".00_06", "Testing button [Trade] in Most traded block")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        check_language(cur_language)
        check_country(cur_country)

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_commodities_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Start test of button '1. Create your account' in 'Steps trading' block")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_08
    def test_08_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All (Except: EL, HU, NL). License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.03", "Education > Menu item [Commodities trading]",
            ".00_08", "Testing button [1. Create your account] in block [Steps trading]")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        check_language(cur_language)

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_commodities_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = BlockStepTrading(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Start test of button in block [Horizontal banner]")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_09
    def test_09_block_hor_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check the [Button] on the Horizontal banner at the bottom of the page.
        For "Authorized user" role:
        The trading platform page is opened depend on the banner [type-id]:
                Live mode if the banner in the Live mode banners list
                Demo mode if the banner in the Demo mode banners list
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.03", "Education > Menu item [Commodities trading]",
            ".00_09", "Testing button in block [Horizontal banner]")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        check_language(cur_language)
        if cur_language in ["", "cn"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # банеры должны открываться в Demo mode for US_00
        banner00_hor_tpd = ['103', '167', '252', '291', '197', '427']
        # банеры должны открываться в Live mode for US_00
        banner00_hor_tp = ['378', '390', '428', '220']
        # банеры должны открываться в Demo mode for US_01
        banner01_hor_tpd = []
        # банеры должны открываться в Live mode for US_01
        banner01_hor_tp = []

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_commodities_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = ButtonOnHorizontalBanner(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link,
                                        banner00_hor_tpd, banner00_hor_tp, banner01_hor_tpd, banner01_hor_tp)

    @allure.step("Start test of button in block [Vertical banner]")
    # @pytest.mark.skip(reason="Skipped for debugging")
    @pytest.mark.test_10
    def test_10_block_vert_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
                Check the [Button] on the Vertical side banner at the bottom of the page.
                For "Authorized user" role:
                The trading platform page is opened depend on the banner [type-id]:
                        Live mode if the banner in the Live mode banners list
                        Demo mode if the banner in the Demo mode banners list
                """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.03", "Education > Menu item [Commodities trading]",
            ".00_10", "Testing button in block [Vertical banner]")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        check_language(cur_language)
        if cur_language in ["", "ar", "it", "cn"]:
            Common().skip_test_for_language(cur_language)

        # test_element.arrange_0()
        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # банеры должны открываться в Demo mode for US_00
        banner00_ver_tpd = ['505', '221', '389']
        # банеры должны открываться в Live mode for US_00
        banner00_ver_tp = ['166', '196', '292', '377', '388', '425']
        # банеры должны открываться в Demo mode for US_01
        banner01_ver_tpd = []
        # банеры должны открываться в Live mode for US_01
        banner01_ver_tp = []

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_commodities_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = ButtonOnVerticalBanner(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link, banner00_ver_tpd,
                                        banner00_ver_tp, banner01_ver_tpd, banner01_ver_tp)

    @allure.step("Start pretest")
    def test_99_commodities_trading_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.03", "Education > Menu item [Commodities trading]",
            ".00_99", "Pretest for US_11.02.03.01")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        check_language(cur_language)
        if cur_language in ["ar", "fr", "cn", "zh"]:
            Common().skip_test_for_language(cur_language)

        if count == 0:
            pytest.skip("The list of Share Trading links is already created")

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        page_menu.open_education_commodities_trading_menu(d, cur_language, cur_country, main_page_link)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-02-03_Commodities_trading/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)

        Common().creating_file_of_hrefs("Commodities trading", list_items, file_name)

        count -= 1
