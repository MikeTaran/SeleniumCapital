import pytest
import allure
from datetime import datetime

from pages.common import Common
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonDownloadAppStore import ButtonDownloadAppStore
from pages.Elements.ButtonExploreWebPlatform import ButtonExploreWebPlatform
from pages.Elements.ButtonGetItOnGooglePlay import ButtonGetItOnGooglePlay
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from pages.Menu.menu import MenuSection
from pages.Elements.AssertClass import AssertClass
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from src.src import CapitalComPageSrc


@pytest.fixture()
def cur_time():
    return str(datetime.now())


@pytest.mark.us_11_03_03
class TestTrendTrading:
    page_conditions = None

    @allure.step("Start test of button [Start Trading] on the Main banner")
    @pytest.mark.test_03
    def test_03_button_start_trading_main_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading]
        Language: En. License: All.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.03", "Education > Menu item [Trend Trading]",
            ".00_03", "Testing button [Start Trading] in the Main banner 'What is trend trading?'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Try demo] on Main banner")
    @pytest.mark.test_04
    def test_04_button_try_demo_main_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on Main banner
        Language: En. License: All.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.03", "Education > Menu item [Trend Trading]",
            ".00_04", "Testing button [Try demo] on Main banner")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.test_05
    def test_05_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded block
        Language: En. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.03", "Education > Menu item [Trend Trading]",
            ".00_05", "Testing button [Trade] in Most traded block")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Download on the App Store] in Block 'Sign up and trade smart today!'")
    @pytest.mark.test_06
    def test_06_button_download_on_the_app_store(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Download on the App Store] in Block "Sign up and trade smart today!"
        Language: En. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.03", "Education > Menu item [Trend Trading]",
            ".00_06", "Test button [Download on the App Store] in Block \"Sign up and trade smart today!\"")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = ButtonDownloadAppStore(d, link)
        test_element.arrange_(link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")
        test_element = AssertClass(d, link, bid)
        test_element.assert_app_store(d, link)

    @allure.step("Start test of button [Get it on Google Play] in Block 'Sign up and trade smart today!'")
    @pytest.mark.test_07
    def test_07_button_get_it_on_google_play(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Get it on Google Play] in Block "Sign up and trade smart today!"
        Language: En. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.03", "Education > Menu item [Trend Trading]",
            ".00_07", "Test button [Get it on Google Play] in Block \"Sign up and trade smart today!\"")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = ButtonGetItOnGooglePlay(d, link)
        test_element.arrange_(link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link, bid)
        test_element.assert_google_play(d, link)

    @allure.step("Start test of button [Explore Web Platform] in Block 'Sign up and trade smart today!'")
    @pytest.mark.test_08
    def test_08_button_explore_web_platform(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Explore Web Platform] in Block "Sign up and trade smart today!"
        Language: En. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.03", "Education > Menu item [Trend Trading]",
            ".00_08", "Testing button [Explore Web Platform] in Block \"Sign up and trade smart today!\"")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = ButtonExploreWebPlatform(d, link)
        test_element.arrange_(link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link, bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup_form_on_the_trading_platform(d)
            case "NoAuth":
                test_element.assert_login_form_on_the_trading_platform(d)
            case "Auth":
                test_element.assert_trading_platform_v4(d, link)

    @allure.step("Start test of button [1. Create & verify your account] in Block 'Steps trading'")
    @pytest.mark.test_09
    def test_09_create_and_verify_your_account_button_in_block_steps_trading(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create & verify your account] in block 'Steps trading'
        Language: En. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.03", "Education > Menu item [Trend Trading]",
            ".00_09", "Testing button [1. Create & verify your account] in Block 'Steps trading'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)
