import allure
import pytest

from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.BlockStepTrading import BlockStepTrading
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.mark.us_11_01_01
class TestLearningHub:
    page_conditions = None

    @allure.step("Start test_11.01.01_01 button '1. Create your account' in the block [Steps trading].")
    @pytest.mark.test_01
    def test_01_create_your_account(
            self, worker_id, d, cur_role, cur_language, cur_country, cur_login, cur_password):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.01", "Education > Menu Item [Learning hub]",
            ".00_01", "Testing button [1. Create your account] in block [Steps trading]")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        menu.menu_education_move_focus(d, cur_language, cur_country)
        link = menu.sub_menu_learning_hub_move_focus_click(d, cur_language, cur_country)

        test_element = BlockStepTrading(d, link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, link)
