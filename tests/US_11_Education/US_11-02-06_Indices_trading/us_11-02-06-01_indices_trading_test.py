import logging

import pytest
import allure

from pages.common import Common
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.Elements.AssertClass import AssertClass

logger = logging.getLogger()


def pytest_generate_tests(metafunc):

    file_name = "tests/US_11_Education/US_11-02-06_Indices_trading/list_of_href.txt"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_02_06_01
class TestIndicesTrading:
    page_conditions = None

    @staticmethod
    def only_four_tests(cur_item_link):
        if cur_item_link in ("https://capital.com/trade-indices",
                             "https://capital.com/trade-nasdaq",
                             "https://capital.com/ar/trade-indices",
                             "https://capital.com/de/indizeshandel",
                             "https://capital.com/es/trade-indices",
                             "https://capital.com/it/trading-su-indici",
                             "https://capital.com/cn/trade-indices"):
            logger.info(f"There is no test item on this page")
            logger.info(f"====== SKIP testing page {cur_item_link} ======")
            pytest.skip("There is no test item on this page")

    @staticmethod
    def not_for_the_sixth_test(cur_item_link):
        if cur_item_link in ("https://capital.com/trade-asx-200",
                             "https://capital.com/de/trade-asx-200",
                             "https://capital.com/de/trade-dax",
                             "https://capital.com/de/trade-nikkei225",
                             "https://capital.com/es/trade-dax",
                             "https://capital.com/it/fare-trading-nikkei-225"):
            logger.info(f"There is no test item on this page")
            logger.info(f"====== SKIP testing page {cur_item_link} ======")
            pytest.skip("There is no test item on this page")

    # @allure.step("Start test of button [Start trading] on Main banner")
    # @pytest.mark.test_01
    # def test_01_main_banner_start_trading_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
    #     """
    #     Check: Button [Start Trading] on Main banner
    #     Language: All. License: All.
    #     """
    #     test_title = ("11.02.06", "Education > Menu item [Indices Trading]", ".01_01",
    #                   "Testing button [Start Trading] on Main banner")
    #
    #     logger.info(f"====== START testing {', '.join(test_title)} ======")
    #
    #     bid = build_dynamic_arg_v4(
    #         d, worker_id, cur_language, cur_country, cur_role, *test_title)
    #
    #     page_conditions = Conditions(d, "")
    #     page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = MainBannerStartTrading(d, cur_item_link)
    #     test_element.arrange_(d, cur_item_link)
    #
    #     if not test_element.element_click():
    #         logger.warning(f"Testing element is not clicked")
    #         logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
    #         pytest.fail("Testing element is not clicked")
    #
    #     test_element = AssertClass(d, cur_item_link)
    #     match cur_role:
    #         case "NoReg":
    #             test_element.assert_signup(d, cur_language, cur_item_link)
    #         case "NoAuth":
    #             test_element.assert_login(d, cur_language, cur_item_link)
    #         case "Auth":
    #             test_element.assert_trading_platform_v4(d, cur_item_link)
    #
    #     logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [Start trading] on Main banner")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link):
        """
        Check: Button [Start Trading] on Main banner
        Language: EN, AR, DE, ES, IT, CN, RU, ZH. License: All.
        """
        test_title = ("11.02.06", "Education > Menu item [Indices Trading]", ".01_01",
                      "Testing button [Start Trading] on Main banner")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "ar", "de", "es", "it", "cn", "ru", "zh"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.test_03
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """

        test_title = ("11.02.06", "Education > Menu item [Indices Trading]",
                      ".01_03", "Testing button [Trade] in Most traded block")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        if cur_country == 'gb':
            logger.info(f"This test is not supported on UK location")
            logger.info(f"====== SKIP testing {', '.join(test_title)} ======")
            pytest.skip("This test is not supported on UK location")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_elements_list = test_element.arrange_v2_()
        for index, element in enumerate(test_elements_list):
            logger.info(f"Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                logger.warning(f"Testing element is not clicked")
                logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
                pytest.fail("Testing element is not clicked")
            check_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    check_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    check_element.assert_trading_platform_v4(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [1. Create & verify your account] in Block 'Steps trading'")
    @pytest.mark.test_04
    def test_04_create_and_verify_your_account_button_in_block_steps_trading(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [1. Create & verify your account] in block 'Steps trading'
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Education > Menu item [Indices Trading]",
                      ".01_04", "Testing button [1. Create & verify your account] in Block 'Steps trading'")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click():
            logger.warning(f"Testing element is not clicked")
            logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [Get started] on Sticky bar")
    @pytest.mark.test_05
    def test_05_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [1. Get started] on Sticky bar
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Education > Menu item [Indices Trading]",
                      ".01_05", "Testing button [Get started] on Sticky bar")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        self.only_four_tests(cur_item_link)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetStartedOnStickyBar(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click():
            logger.warning(f"Testing element is not clicked")
            logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [Start trading] in content block")
    @pytest.mark.test_06
    def test_06_start_trading_in_content_block_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start trading] in article
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Education > Menu item [Indices Trading]",
                      ".01_06", "Testing button [Start trading] in Content block")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        self.only_four_tests(cur_item_link)
        self.not_for_the_sixth_test(cur_item_link)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, cur_item_link)
        test_elements_list = test_element.arrange_v4()

        for index, element in enumerate(test_elements_list):
            logger.info(f"Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                logger.warning(f"Testing element is not clicked")
                logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
                pytest.fail("Testing element is not clicked")

            check_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    check_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    check_element.assert_trading_platform_v4(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [Sell] in content block")
    @pytest.mark.test_07
    def test_07_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Sell] in content block
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Education > Menu item [Indices Trading]",
                      ".01_07", "Testing button [Sell] in content block")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        self.only_four_tests(cur_item_link)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click(cur_role):
            logger.warning(f"Testing element is not clicked")
            logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")

    @allure.step("Start test of button [Buy] in content block")
    @pytest.mark.test_08
    def test_08_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Buy] in content block
        Language: All. License: All.
        """
        test_title = ("11.02.06", "Education > Menu item [Indices Trading]",
                      ".01_08", "Testing button [Buy] in content block")

        logger.info(f"====== START testing {', '.join(test_title)} ======")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        self.only_four_tests(cur_item_link)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click(cur_role):
            logger.warning(f"Testing element is not clicked")
            logger.info(f"====== FAIL testing {', '.join(test_title)} ======")
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

        logger.info(f"====== END testing {', '.join(test_title)} ======")
