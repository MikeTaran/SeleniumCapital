"""
-*- coding: utf-8 -*-
@Time    : 2023/05/24 13:40
@Author  : Alexander Tomelo
"""
import pytest
import allure
import random  # for new method
from datetime import datetime
from conf import QTY_LINKS
from pages.common import Common
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v3
from pages.conditions import Conditions
from pages.Education.forex_trading_locators import ForexTradingItem
from src.src import CapitalComPageSrc
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.BlockStepTrading import BlockStepTrading

count = 1
cur_page_url = ""


@pytest.mark.us_11_02_04
class TestForexTradingMainPage:
    # def __init__(self):
    #     self.forex_trading_main_page_url = conf.URL
    #     self.page_conditions = None
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01_main_banner_start_trading_button(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password
    ):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        global cur_page_url

        build_dynamic_arg_v3(
            self,
            d,
            worker_id,
            cur_language,
            cur_country,
            cur_role,
            "11.02.04",
            "Education > Menu item [Forex trading]",
            ".00_01",
            "Testing button [Start Trading] on Main banner",
        )

        if cur_language not in ["", "ar", "de", "es", "fr", "it", "cn", "ru", "zh"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d,
            CapitalComPageSrc.URL,
            # forex_trading_main_page_url,
            "",
            cur_language,
            cur_country,
            cur_role,
            cur_login,
            cur_password,
        )

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_forex_trading_menu(d, cur_language, main_page_link)

        test_element = MainBannerStartTrading(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_02_main_banner_try_demo_button(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password
    ):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        global cur_page_url

        build_dynamic_arg_v3(
            self,
            d,
            worker_id,
            cur_language,
            cur_country,
            cur_role,
            "11.02.04",
            "Education > Menu item [Forex trading]",
            ".00_02",
            "Testing button [Try demo] on Main banner",
        )

        if cur_language not in ["", "ar", "de", "es", "fr", "it", "cn", "ru", "zh"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d,
            CapitalComPageSrc.URL,
            # forex_trading_main_page_url,
            "",
            cur_language,
            cur_country,
            cur_role,
            cur_login,
            cur_password,
        )

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_forex_trading_menu(d, cur_language, main_page_link)

        test_element = MainBannerTryDemo(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Sell] in content block")
    def test_04_content_block_button_sell(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password
    ):
        """
        Check: Button [Sell] in content block
        Language: All. License: All.
        """
        global cur_page_url

        build_dynamic_arg_v3(
            self,
            d,
            worker_id,
            cur_language,
            cur_country,
            cur_role,
            "11.02.04",
            "Education > Menu item [Forex trading]",
            ".00_04",
            "Testing button [Sell] in content block",
        )

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)

        if cur_language not in ["", "de", "es", "it", "cn", "ru"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d,
            CapitalComPageSrc.URL,
            "",
            cur_language,
            cur_country,
            cur_role,
            cur_login,
            cur_password,
        )

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_forex_trading_menu(d, cur_language, main_page_link)

        test_element = SellButtonContentBlock(d, cur_page_url)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_page_url)

    def test_05_content_block_button_buy(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password
    ):
        """
        Check: Button [Buy] in content block
        Language: All. License: All.
        """
        global cur_page_url

        build_dynamic_arg_v3(
            self,
            d,
            worker_id,
            cur_language,
            cur_country,
            cur_role,
            "11.02.04",
            "Education > Menu item [Forex trading]",
            ".00_05",
            "Testing button [Buy] in content block",
        )

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)

        if cur_language not in ["", "de", "es", "it", "cn", "ru"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d,
            CapitalComPageSrc.URL,
            "",
            cur_language,
            cur_country,
            cur_role,
            cur_login,
            cur_password,
        )

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_forex_trading_menu(d, cur_language, main_page_link)

        test_element = BuyButtonContentBlock(d, cur_page_url)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    def test_06_most_traded_trade_button(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password
    ):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        global cur_page_url

        build_dynamic_arg_v3(
            self,
            d,
            worker_id,
            cur_language,
            cur_country,
            cur_role,
            "11.02.04",
            "Education > Menu item [Forex trading]",
            ".00_06",
            "Testing button [Trade] in Most traded block",
        )

        if cur_country in ["gb"]:
            Common().skip_test_for_country(cur_country)
        if cur_language not in ["", "ar", "de", "es", "fr", "it", "cn", "ru", "zh"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d,
            CapitalComPageSrc.URL,
            # forex_trading_main_page_url,
            "",
            cur_language,
            cur_country,
            cur_role,
            cur_login,
            cur_password,
        )

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_forex_trading_menu(d, cur_language, main_page_link)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button '1. Create your account' in 'Steps trading' block")
    def test_07_block_steps_trading_button_1_create_your_account(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password
    ):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        global cur_page_url

        build_dynamic_arg_v3(
            self,
            d,
            worker_id,
            cur_language,
            cur_country,
            cur_role,
            "11.02.04",
            "Education > Menu item [Forex trading]",
            ".00_07",
            "Testing button [1. Create your account] in block [Steps trading]",
        )

        if cur_language not in ["", "ar", "de", "es", "fr", "it", "cn", "ru", "zh"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d,
            CapitalComPageSrc.URL,
            "",
            cur_language,
            cur_country,
            cur_role,
            cur_login,
            cur_password,
        )

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_forex_trading_menu(d, cur_language, main_page_link)

        test_element = BlockStepTrading(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start pretest")
    def test_99_forex_trading_item_pretest(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password
    ):
        global count
        global cur_page_url

        build_dynamic_arg_v3(
            self,
            d,
            worker_id,
            cur_language,
            cur_country,
            cur_role,
            "11.02.04",
            "Education > Menu item [Forex trading]",
            ".00_99",
            "Pretest for US_11.02.04.01",
        )

        if cur_language not in ["", "ar", "de", "es", "fr", "it", "cn", "ru", "zh"]:
            Common().skip_test_for_language(cur_language)

        if count == 0:
            pytest.skip("The list of Forex trading links is already created")

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d,
            CapitalComPageSrc.URL,
            # forex_trading_main_page_url,
            "",
            cur_language,
            cur_country,
            cur_role,
            cur_login,
            cur_password
        )

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_forex_trading_menu(d, cur_language, main_page_link)

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-02-04_Forex_trading/list_of_href.txt"
        list_items = d.find_elements(*ForexTradingItem.ITEM_LIST)

        count_in = len(list_items)
        print(f"{datetime.now()}   Forex trading include {count_in} item(s) on page")
        file = None

        try:
            file = open(file_name, "w")
            count_out = 0
            url_prev = ""
            if count_in > 0:
                for i in range(QTY_LINKS):
                    if i < count_in:
                        while True:
                            k = random.randint(1, count_in - 1)
                            item = list_items[k]
                            url = item.get_property("href")
                            print(f"{datetime.now()}   {url}")
                            if url != url_prev:
                                break
                        file.write(url + "\n")
                        url_prev = url
                        print(f"{datetime.now()}   {url}")
                        count_out += 1
        finally:
            file.close()
            del file

        print(f"{datetime.now()}   Test data include {count_out} item(s)")
        if count_in != 0:
            print(f"{datetime.now()}   The test coverage = {count_out/count_in*100} %")
        else:
            print(f"{datetime.now()}   The test coverage = 0 %")
        count -= 1
