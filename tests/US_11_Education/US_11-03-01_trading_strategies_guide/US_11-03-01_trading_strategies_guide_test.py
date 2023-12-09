import allure
import pytest
from datetime import datetime
import random  # for new method
from conf import QTY_LINKS
from pages.Education.Trading_strategies_guide_locators import TradingStrategiesContentList
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v3
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass
from src.src import CapitalComPageSrc

count = 1


@pytest.fixture()
def cur_time():
    return str(datetime.now())


@pytest.mark.us_11_03_01
class TestTradingStrategiesGuides:
    page_conditions = None

    @allure.step("Start test_11.03.01_01 of button [Start Trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading]
        Language: All. License: All.
        """
        link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                    "11.03.01",
                                    "Education > Menu item [Trading Strategies Guides]",
                                    ".00_01",
                                    "Testing button [Start Trading] on Main banner")

        if cur_language not in ["", "de", "es", "it", "cn", "zh", "ru"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test_11.03.01_02 of button [Try demo] on Main banner")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                    "11.03.01",
                                    "Education > Menu item [Trading Strategies Guides]",
                                    ".00_02",
                                    "Testing button [Try demo] on Main banner")

        if cur_language not in ["", "de", "es", "it", "cn", "zh", "ru"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test_11.03.01_03 of buttons [Trade] in Most traded block")
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.01",
                             "Education > Menu item [Trading Strategies Guides]",
                             ".00_03",
                             "Testing button [Trade] in Most traded block")

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        if cur_language not in ["", "de", "es", "it", "cn", "zh", "ru"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test_11.03.01_04 button 'Create_verify_your_account' on the page.")
    def test_04_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Steps trading -> button [1. Create your account]
        Language: All. License: All.
        """
        link = build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                                    "11.03.01",
                                    "Education > Menu item [Trading Strategies Guides]",
                                    ".00_04",
                                    "Testing button [1. Create your account] in block [Steps trading]")

        if cur_language not in ["", "de", "es", "it", "cn", "zh", "ru"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start pretest")
    def test_99_trading_strategies_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):

        global count

        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.01", "Education > Menu item [Trading Strategies Guides]",
                             ".00_99", "Pretest for US_11.03.01.01")

        if cur_language not in ["", "de", "es", "it", "zh", "ru"]:
            Common().skip_test_for_language(cur_language)

        if count == 0:
            pytest.skip("The list of Trading courses links is already created")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-03-01_trading_strategies_guide/list_of_href.txt"
        list_items = d.find_elements(*TradingStrategiesContentList.LISTS)

        count_in = len(list_items)
        print(f"{datetime.now()}   Trading Strategies Guide page include {count_in} lists item(s)")  # for new method
        file = None

        try:
            file = open(file_name, "w")
            count_out = 0
            url_prev = ""
            if count_in > 0:
                for i in range(QTY_LINKS):
                    if i < count_in:
                        while True:
                            k = random.randint(0, count_in - 1)
                            item = list_items[k]
                            url = item.get_property("href")
                            print(f"{datetime.now()}   {url}")
                            if url != url_prev:
                                break
                        file.write(url + "\n")
                        url_prev = url
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
