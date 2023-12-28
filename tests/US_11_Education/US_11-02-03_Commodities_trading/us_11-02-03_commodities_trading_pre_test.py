"""
-*- coding: utf-8 -*-
@Time    : 2023/04/19 17:00 GMT+3
@Author  : Suleyman Alirzaev
"""
# import os.path
import pytest
import allure
from datetime import datetime
from pages.common import Common
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.testing_elements_locators import SubPages

count = 1


@pytest.mark.us_11_02_03_pre
# @allure.epic('US_11.02.03 | Find materials pages in "Commodities trading" menu')
class TestCommoditiesTradingPretest:
    page_conditions = None

    @allure.step("Start pretest")
    def test_commodities_trading_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.03", "Education > Menu item [Commodities trading]",
            ".00_99", "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "ar", "de", "es", "fr", "it",
                                                                               "pl", "cn", "nl", "ro", "ru", "zh"])
        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_commodities_trading_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-02-03_Commodities_trading/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)

        Common().creating_file_of_hrefs("Commodities trading", list_items, file_name)

        count -= 1
