import allure
import pytest
from pages.Menu.menu import MenuSection
from pages.Elements.BlockStepTrading import BlockStepTrading
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.mark.us_11_01_02
class TestBasicsOfTrading:
    page_conditions = None

    @allure.step("Start test_11.01.02_01 button '1. Create & verify your account'")
    @pytest.mark.test_01
    def test_01_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create & verify account]
        Language: All. License: All. Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.02", "Education > Menu Item [The basics of trading]",
            ".00_01", "Testing button [1. Create your account] in block [Steps trading]")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        cur_page_url = page_menu.sub_menu_basics_of_trading_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)
