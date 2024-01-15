"""
-*- coding: utf-8 -*-
@Time    : 18/12/2023
@Author  : Mike Taran
"""

import os
import subprocess
import re
from datetime import datetime

import allure
import pytest

# import pytest
# import pytest_timeout

from tests.ReTests.retest_data import us_data
from tests.ReTests.GoogleSheets.googlesheets import GoogleSheet

test_id = None
browser_name = None
us = None
path = None
num_test = None
lang = None
country = None
role = None
url = None


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """

    list_number_rows = list()
    start_row = 5
    gs = GoogleSheet()
    qty_of_bugs = gs.get_cell_values("A2")
    del gs
    end_row = start_row + int(qty_of_bugs[0][0])
    for num_row in range(start_row, end_row):
        list_number_rows.append(num_row)

    print(f"\n{datetime.now()}   Список номеров строк = {list_number_rows}")

    metafunc.parametrize("number_of_row", list_number_rows, scope="class")


class TestReTests:

    @allure.step("Start TestCase from ReTests")
    # @pytest.mark.timeout(timeout=240, method="thread")
    def test_retests(self, gs, number_of_row):

        print(f"\n\n\n{datetime.now()}   0. Get Values row =>")
        print(f"{datetime.now()}   Row # = {number_of_row}")
        row_values = gs.get_row_values(number_of_row)
        print(f"{datetime.now()}   Row Values = \n{row_values[0]}")

        # pre-test
        pretest(row_values[0], number_of_row, gs)

        # Запуск pytest с параметрами
        output, error = run_pytest()

        # проверка результатов тестирования
        gs_out = check_results(output, error)

        # заполнение Google Sheets по-строчно
        result = gs.update_range_values(f'V{number_of_row}', [gs_out])

        assert True


@allure.step("Pretest")
def pretest(row_loc, number_of_row, gs):
    global test_id, browser_name, us, path, num_test, lang, country, role, url

    print(f"\n{datetime.now()}   1. Run pretest =>")
    print(f"\n{datetime.now()}   row_loc = \n{row_loc}")

    # аргументы командной строки
    try:
        test_id = row_loc[0]
        browser_name = row_loc[2]
        us = row_loc[3]
        path = us_data.us_data[us]
        num_test = row_loc[4]
        lang = '' if row_loc[5] == 'en' else row_loc[5]
        country = row_loc[6]
        role = row_loc[8]
        url = row_loc[9]
        # num_bug = row_loc[12]
    except KeyError:
        print(f"\n{datetime.now()}   =>  Не корректные входные данные из таблицы WATC_BugsReport")
        gs.update_range_values(f'V{number_of_row}', [["skipped"]])
        pytest.skip()

    print(f"\n{datetime.now()}   => 1. Pretest finished")


@allure.step("Run aurotest with Bid parameters")
def run_pytest():
    global test_id, browser_name, us, path, num_test, lang, country, role, url

    print(f"\n{datetime.now()}   2. Run run_pytest with Bid = {test_id} from row =>")

    # print(f"\n{datetime.now()}   2.1. Run hw_info.py in subprocess =>")
    # # формирование командной строки и запуск hw_info.py, как subprocess
    # command = "poetry run python3 tests/hwinfo.py"
    # print(f"\n{datetime.now()}   Run command: \n{command}")
    # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # hwinfo_stdout, stderr = process.communicate()
    # hwinfo_out = hwinfo_stdout.decode('utf-8')
    # print(f"{datetime.now()} hwinfo output: \n{hwinfo_out}")
    # print(f"{datetime.now()}   => 2.1. Finished subprocess hw_info.py")

    print(f"\n{datetime.now()}   2.2. Run poetry run pytest ... in subprocess =>")
    retest = True
    # получение корня проекта
    host = "\\".join(os.getcwd().split('\\')[:-2]) + '\\'
    # host = "\\".join(os.getcwd().split('\\')) + '\\'            # for debugging
    # формирование командной строки и запуск pytest, как subprocess
    command = (f"poetry run pytest"
               f" --retest={retest}"
               f" --browser_name={browser_name}"
               f" --lang={lang}"
               f" --country={country}"
               f" --role={role}")
    if us[-3::] != ".00":
        command += f" --tpi_link={url}"
    command += f" -m test{num_test}"
    command += " -v"
    # command += " --no-summary -v"
    command += f" {host}{path}"
    # command += f" --json-report --json-report-omit keywords streams"

    print(f"\n{datetime.now()}   Run command: \n{command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # print(f"\n{datetime.now()}   stdout = '{stdout}'")
    # print(f"\n{datetime.now()}   stderr = '{stderr}'")
    print(f"\n{datetime.now()}   => 2.2. pytest ... as subprocess finished")
    print(f"\n{datetime.now()}   => 2. Autotest with Bid = {test_id} from row finished")

    return stdout, stderr


def check_results(output, error):
    print(f"\n{datetime.now()}   3. Run check_results =>")
    # Проверка наличия ошибок при выполнении
    gs_out = ["WebDriver Error"]

    if error:
        print(f"{datetime.now()}   Ошибка: \n{error.decode('utf-8')}")
        gs_out = ['Stdout error']
        print(f"{datetime.now()}   => Текущий тест: skipped")
        return gs_out
    else:
        test_results = output.decode('utf-8')
        print(f"{datetime.now()}   test_results: \n{test_results}")

    # Проверка на выбор хотя бы одного теста
    failed_match_selected = re.search(r"(\d+ selected)", test_results)
    if failed_match_selected:
        selected = failed_match_selected.group(1)
        if selected == "0 selected":
            print(f"{datetime.now()}   => Для текущего теста не выбрано ни одного ТС")
            print(f"{datetime.now()}   => Текущий тест: skipped")
            gs_out = ['0 TC selected']
            return gs_out
    else:
        print(f"{datetime.now()}   => Для текущего теста не выбрано ни одного ТС")
        print(f"{datetime.now()}   => Текущий тест: skipped")
        gs_out = ['No one TC selected']
        return gs_out

    # Проверка на Failed
    failed_match = re.search(r"(\d+ failed)", test_results)
    if failed_match:
        failed = failed_match.group(1)
        print(f"{datetime.now()}   => Текущий тест: {failed}")
        gs_out = ['failed']

    # Проверка на Broken
    broken_match = re.search(r"(\d+ broken)", test_results)
    if broken_match:
        broken = broken_match.group(1)
        print(f"{datetime.now()}   => Текущий тест: {broken}")
        gs_out = ['broken']

    # Проверка на Passed
    passed_match = re.search(r"(\d+ passed)", test_results)
    if passed_match:
        passed = passed_match.group(1)
        print(f"{datetime.now()}   => Текущий тест: {passed}")
        gs_out = ['passed']

    # Проверка на Skipped
    skipped_match = re.search(r"(\d+ skipped)", test_results)
    if skipped_match:
        skipped = skipped_match.group(1)
        print(f"{datetime.now()}   => Текущий тест: {skipped}")
        gs_out = ['skipped']

    print(f"\n{datetime.now()}   => 3. check_results finished")

    return gs_out
