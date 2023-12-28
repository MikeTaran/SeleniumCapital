import pytest
import allure
from datetime import datetime

from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonDownloadAppStore import ButtonDownloadAppStore
from pages.Elements.ButtonExploreWebPlatform import ButtonExploreWebPlatform
from pages.Elements.ButtonGetItOnGooglePlay import ButtonGetItOnGooglePlay
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.Elements.AssertClass import AssertClass


class USLink:
    user_story_menu_link = None

    def get_us_link(self, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        if cur_language not in [""]:
            pytest.skip(f"This test is not for {cur_language} language")

        page_conditions = Conditions(d, "")
        main_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        if not self.user_story_menu_link:
            page_menu = MenuSection(d, main_link)
            page_menu.menu_education_move_focus(d, cur_language)
            us_link = page_menu.sub_menu_swing_trading_move_focus_click(d, cur_language)
            self.user_story_menu_link = us_link
        return self.user_story_menu_link


@pytest.mark.us_11_03_05
class TestSwingTrading:
    page_conditions = None
    us_link = USLink()

    @allure.step("Start test of button [Start trading] on Main banner")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.05", "Education > Menu item [Swing Trading]",
            ".00_01", "Testing button [Start Trading] on Main banner")

        link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)

    @allure.step("Start test of button [Try demo] on Main banner")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.05", "Education > Menu item [Swing Trading]",
            ".00_02", "Testing button [Try demo] on Main banner")

        link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link, demo=True)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.test_03
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.05", "Education > Menu item [Swing Trading]",
            ".00_03", "Testing button [Trade] in Most traded block")

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, link)
        test_elements_list = test_element.arrange_v2_()
        for index, element in enumerate(test_elements_list):
            print(f"\n{datetime.now()}   Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                pytest.fail("Testing element is not clicked")
            check_element = AssertClass(d, link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, link)
                case "NoAuth":
                    check_element.assert_login(d, cur_language, link)
                case "Auth":
                    check_element.assert_trading_platform_v3(d, link)

    @allure.step("Start test of button [Download on the App Store] in Block 'Sign up and trade smart today!'")
    @pytest.mark.test_04
    def test_04_button_download_on_the_app_store(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Download on the App Store] in Block "Sign up and trade smart today!"
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.05", "Education > Menu item [Swing Trading]",
            ".00_04", "Test button [Download on the App Store] in Block \"Sign up and trade smart today!\"")

        link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonDownloadAppStore(d, link)
        test_element.arrange_(link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")
        test_element = AssertClass(d, link)
        test_element.assert_app_store(d, link)

    @allure.step("Start test of button [Get it on Google Play] in Block 'Sign up and trade smart today!'")
    @pytest.mark.test_05
    def test_05_button_get_it_on_google_play(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Get it on Google Play] in Block "Sign up and trade smart today!"
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.05", "Education > Menu item [Swing Trading]",
            ".00_05", "Test button [Get it on Google Play] in Block \"Sign up and trade smart today!\"")

        link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonGetItOnGooglePlay(d, link)
        test_element.arrange_(link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        test_element.assert_google_play(d, link)

    @allure.step("Start test of button [Explore Web Platform] in Block 'Sign up and trade smart today!'")
    @pytest.mark.test_06
    def test_06_button_explore_web_platform(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Explore Web Platform] in Block "Sign up and trade smart today!"
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.05", "Education > Menu item [Swing Trading]",
            ".00_06", "Testing button [Explore Web Platform] in Block \"Sign up and trade smart today!\"")

        link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonExploreWebPlatform(d, link)
        test_element.arrange_(link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup_form_on_the_trading_platform(d)
            case "NoAuth":
                test_element.assert_login_form_on_the_trading_platform(d)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)

    @allure.step("Start test of button [1. Create & verify your account] in Block 'Steps trading'")
    @pytest.mark.test_07
    def test_07_create_and_verify_your_account_button_in_block_steps_trading(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create & verify your account] in block 'Steps trading'
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.03.05", "Education > Menu item [Swing Trading]",
            ".00_07", "Testing button [1. Create & verify your account] in Block 'Steps trading'")

        link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)
