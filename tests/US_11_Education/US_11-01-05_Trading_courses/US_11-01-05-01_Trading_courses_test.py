from datetime import datetime

import allure
import pytest

from pages.common import Common
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonCreateDemoAccBlockBuildYourSkills import BuildYourSkillsButtonCreateDemoAccount
from pages.Elements.ButtonTryDemoBlockLearnFirstTradeCFD import BlockLearnFistTradeCFDTryDemo
from pages.Elements.AssertClass import AssertClass
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    file_name = "tests/US_11_Education/US_11-01-05_Trading_courses/list_of_href.txt"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_01_05
class TestTradingCoursesItem:
    page_conditions = None

    @allure.step("Start test_11.01.05.01_02 Click button [Create a demo account] "
                 "in block 'Build your skills with a risk-free demo account.'")
    @pytest.mark.test_02
    def test_02_create_demo_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Block "Build your skills" -> button [Create a demo account]
        Language: All. License: All. Role: All
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.05", "Education > Menu Item [Trading courses]",
            ".01_02", "Testing button [Create a demo account] in block 'Build your skills ...'")

        if cur_language not in [""]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuildYourSkillsButtonCreateDemoAccount(d, cur_item_link)
        test_element.arrange(cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link, bid)
        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, True)

    @allure.step("Start test_11.01.05.01_03 button [Try demo] in block 'Learn first. Trade CFDs ...")
    @pytest.mark.test_03
    def test_03_try_demo(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Block "Learn first ..." -> button [Try demo]
        Language: All. License: All. Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.05", "Education > Menu Item [Trading courses]",
            ".01_03", "Testing button [Try demo] in block 'Learn first. Trade CFDs ...'")

        if cur_language not in [""]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockLearnFistTradeCFDTryDemo(d, cur_item_link)
        test_element.arrange(cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link, bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, True)

    @allure.step("Start test_11.01.05.01_04 button [1. Create your account] in block 'Steps trading'.")
    @pytest.mark.test_04
    def test_04_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Steps trading -> button [1. Create your account]
        Language: All. License: All. Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.05", "Education > Menu Item [Trading courses]",
            ".01_04", "Testing button [1. Create your account] in block [Steps trading]")

        if cur_language in ["ar"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)
