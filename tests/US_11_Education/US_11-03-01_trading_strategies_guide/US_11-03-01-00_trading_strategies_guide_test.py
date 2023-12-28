import allure
import pytest
from datetime import datetime
from pages.Education.Trading_strategies_guide_locators import TradingStrategiesContentList
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from pages.Elements.BlockStepTrading import BlockStepTrading
from src.src import CapitalComPageSrc

count = 1


@pytest.fixture()
def cur_time():
    return str(datetime.now())


@pytest.mark.us_11_03_01
class TestTradingStrategiesGuides:
    page_conditions = None

    @allure.step("Start test_11.03.01_01 of button [Start Trading] on Main banner")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading]
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.01", "Education > Menu item [Trading Strategies Guides]",
            ".00_01", "Testing button [Start Trading] on Main banner")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "de", "es", "it", "cn", "ru", "zh"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test_11.03.01_02 of button [Try demo] on Main banner")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.01", "Education > Menu item [Trading Strategies Guides]",
            ".00_02", "Testing button [Try demo] on Main banner")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "de", "es", "it", "cn", "ru", "zh"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test_11.03.01_03 of buttons [Trade] in Most traded block")
    @pytest.mark.test_03
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.01", "Education > Menu item [Trading Strategies Guides]",
            ".00_03", "Testing button [Trade] in Most traded block")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "de", "es", "it", "cn", "ru", "zh"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test_11.03.01_04 button 'Create_verify_your_account' on the page.")
    @pytest.mark.test_04
    def test_04_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Steps trading -> button [1. Create your account]
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.01", "Education > Menu item [Trading Strategies Guides]",
            ".00_04", "Testing button [1. Create your account] in block [Steps trading]")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "de", "es", "it", "cn", "ru", "zh"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
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

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.01", "Education > Menu item [Trading Strategies Guides]",
            ".00_99", "Pretest for US_11.03.01.01")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "de", "es", "it", "ru", "zh"])

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

        Common().creating_file_of_hrefs("Trading Strategies Guide", list_items, file_name, 0)

        count -= 1
