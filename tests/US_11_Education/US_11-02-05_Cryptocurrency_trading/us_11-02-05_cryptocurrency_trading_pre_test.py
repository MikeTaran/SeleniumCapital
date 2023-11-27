"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 19:00 GMT+3
@Author  : Suleyman Alirzaev
"""
# import os.path
import pytest
import allure
import random  # for new method
import conf
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.testing_elements_locators import SubPages

count = 1


@pytest.mark.us_11_02_05_pre
class TestCryptocurrencyTradingPretest:
    page_conditions = None

    def check_language(self, cur_language):
        if cur_language not in ["", "de", "es", "fr", "it", "pl", "ro", "ru", "zh", "cn"]:
            pytest.skip(f"This test is not for {cur_language} language")

    def check_country(self, cur_country):
        if cur_country in ["gb"]:
            pytest.skip(f"This test is not for {cur_country} country")

    @allure.step("Start pretest")
    def test_cryptocurrency_trading_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.02.05_00")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.05", "Educations > Menu item [Cryptocurrency trading]",
                             "00", "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        self.check_language(cur_language)
        self.check_country(cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_cryptocurrency_trading_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-02-05_Cryptocurrency_trading/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)  # for new method

        count_in = len(list_items)
        print(f"{datetime.now()}   Cryptocurrency trading include {count_in} coins items on selected '{cur_language}' "
              f"language")

        file = None
        try:
            file = open(file_name, "w")
            count_out = 0
            if count_in > 0:
                for i in range(conf.QTY_LINKS):
                    if i < count_in:
                        k = random.randint(1, count_in)
                        item = list_items[k - 1]
                        file.write(item.get_property("href") + "\n")
                        count_out += 1

            file.write(d.current_url + "\n")    # для добавления головной страницы
            count_in += 1    # для добавления головной страницы
            count_out += 1    # для добавления головной страницы
            print(f"{datetime.now()}   Plus 1 main page Cryptocurrency trading. Total: {count_in} for testing")
        finally:
            file.close()
            del file

        print(f"{datetime.now()}   Test data include {count_out} item(s)")
        if count_in != 0:
            print(f"{datetime.now()}   The test coverage = {count_out/count_in*100} %")
            count -= 1
        else:
            print(f"{datetime.now()}   The test coverage = 0 %")
