"""
-*- coding: utf-8 -*-
@Time    : 2023/04/11 19:00
@Author  : Alexander Tomelo
"""
from datetime import datetime
import pytest
import allure
from pages.common import Common
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass
from src.src import CapitalComPageSrc
from pages.Education.Glossary_locators import (
    FinancialDictionary,
)

count = 1


@pytest.mark.us_11_01_07
class TestGlossaryOfTradingTerms:

    page_conditions = None

    # def __init__(self, *args, **kwargs):
    #     global count_init
    #     print(f"{datetime.now()}   В классе TestGlossaryItems вызван метод __init__ {self}")
    #     count_init += 1
    # super().__init__(*args, **kwargs)

    @allure.step("Start test of button 'Create your account' in 'Steps trading' block")
    @pytest.mark.test_01
    def test_01(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.07", "Education > Menu item [Glossary of trading terms]",
            ".00_01", "Testing button [1. Create your account] in block [Steps trading]")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if cur_language not in ["", "de", "el", "es", "fr", "it", "hu", "nl", "pl", "ro", "ru", "zh"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        link = page_menu.sub_menu_glossary_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link, bid)
        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, link)

        del test_element
        del page_menu

    @allure.step("Start pretest")
    def test_99_glossary_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07_99")

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.07", "Education > Menu item [Glossary of trading terms]",
            ".00_99", "Pretest for US_11.01.07.01")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if count == 0:
            pytest.skip("The list of Glossary of trading terms links is already created")

        if cur_language not in ["", "de", "el", "es", "fr", "it", "hu", "nl", "pl", "ro", "ru", "zh"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        page_menu.sub_menu_glossary_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-01-07_Glossary/list_of_href.txt"
        list_items = d.find_elements(*FinancialDictionary.ITEM_LIST)

        Common().creating_file_of_hrefs("Glossary of trading terms", list_items, file_name, 0)

        count -= 1
