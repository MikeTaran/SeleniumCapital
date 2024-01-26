import allure
import pytest

from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.BlockStepTrading import BlockStepTrading
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.mark.us_11_02_01
class TestMarketGuides:
    page_conditions = None

    @allure.step("Start test_11.02.01_03 button '1. Create & verify your account' on the page.")
    @pytest.mark.test_01
    def test_01_create_verify_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Block "Steps trading" -> button [1. Create & verify your account]
        Language: En. License: FCA. Role All.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.01", "Education > Menu Item [Market guides]",
            ".00_01", "Testing button [Create your account] in block [Steps trading]")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_market_guides_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)
