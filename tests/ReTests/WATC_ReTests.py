"""
-*- coding: utf-8 -*-
@Time    : 18/12/2023
@Author  : Mike Taran
"""

import os
import subprocess
import re
from datetime import datetime

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
    start_row = 4
    gs = GoogleSheet()
    qty_of_bugs = gs.get_cell_values("A2")
    del gs
    end_row = start_row + int(qty_of_bugs[0][0])
    for num_row in range(start_row, end_row):
        list_number_rows.append(num_row)

    print(f"\n{datetime.now()}   Список номеров строк = {list_number_rows}")

    metafunc.parametrize("number_of_row", list_number_rows, scope="class")


class TestReTests:

    def test_retests(self, d, gs, number_of_row):

        print(f"\n\n\n{datetime.now()}   0. Get Value row =>")
        print(f"Row # = {number_of_row}")
        row_values = gs.get_row_values(number_of_row)
        print(f"Row Value = {row_values[0]}")

        # pre-test
        print(f"\n{datetime.now()}   1. Run pretest =>")
        pretest(row_values[0])

        # Запуск pytest с параметрами
        print(f"\n{datetime.now()}   2. Run run_pytest with parameters from row =>")
        output, error = run_pytest()

        # проверка результатов тестирования
        print(f"\n{datetime.now()}   3. Run check_results =>")
        gs_out = check_results(output, error)

        # заполнение Google Sheets по-строчно
        # ==================
        print(f"\n{datetime.now()}   4. Fixing one row check results into Google Sheet Bugs Report =>")
        result = gs.update_range_values(f'V{number_of_row}', [gs_out])
        print('{0} cells updated.'.format(result.get('totalUpdatedCells')))
        # ==================
        assert True


def pretest(row_loc):
    global test_id, browser_name, us, path, num_test, lang, country, role, url

    # аргументы командной строки
    try:
        test_id = row_loc[0]
        browser_name = row_loc[2]
        us = row_loc[3]
        path = us_data.us_data[row_loc[3]]
        num_test = row_loc[4]
        lang = '' if row_loc[5] == 'en' else row_loc[5]
        country = row_loc[6]
        role = row_loc[8]
        url = row_loc[9]
        # num_bug = row_loc[12]
    except KeyError:
        print("Не корректные входные данные из таблицы WATC_BugsReport")


def run_pytest():
    global test_id, browser_name, us, path, num_test, lang, country, role, url

    retest = True
    # получение корня проекта
    host = "\\".join(os.getcwd().split('\\')[:-2]) + '\\'
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

    print(f"command: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr


def check_results(output, error):
    # Проверка наличия ошибок при выполнении
    test_results = ""
    gs_out = [[]]

    if error:
        print(f"Ошибка: {error.decode('utf-8')}")
    else:
        test_results = output.decode('utf-8')
        print(f"{datetime.now()} test_results: \n{test_results}")

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

    return gs_out
