"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 18:30 GMT+3
@Author  : Suleyman Alirzaev
"""
import pytest
import allure
import random
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.testing_elements_locators import SubPages

first_run_pretest = True


@pytest.mark.us_11_01_04_pre
class TestSpreadBettingGuidePretest:
    page_conditions = None

    @allure.step("Start pretest")
    def test_spread_betting_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global first_run_pretest

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_00")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                                    "11.01.04", "Educations > Menu item [Spread betting guide]",
                                    "00", "Pretest")

        if not first_run_pretest:
            pytest.skip("Пропускаем претест, так как ранее его уже прошли")

        if cur_language not in ["", "es", "ch"]:
            pytest.skip(f"Test section released not for '{cur_language}' language.")
        if cur_country not in ["gb"]:
            pytest.skip(f"Test section released for FCA licence ('{cur_country}' country) only.")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_spread_betting_guide_move_focus_click(d, cur_language)

        file_name = "tests/US_11_Education/US_11-01-04_spread_betting_guide/list_of_href.txt"

        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)

        href_list = list()
        if len(list_items) > 0:
            href_list = list(map(lambda element: element.get_property("href"), list_items))
        else:
            href_list.append(d.current_url)

        count_all = len(href_list)
        print(f"Spread betting guide include {count_all} items on selected '{cur_language}' language")
        # выбираем не более 3-х случайных элементов
        random_list = random.sample(href_list, 3 if count_all >= 3 else count_all)
        with open(file_name, "w", encoding='UTF-8') as f:
            for val in random_list:
                f.write(val + "\n")
        print(f"{datetime.now()}   Test data include {len(random_list)} Spread betting guide item(s)")
        print(f"{datetime.now()}   The probability of test coverage = {len(random_list) / count_all * 100} %")
        first_run_pretest = False
