"""
-*- coding: utf-8 -*-
@Time    : 2023/12/24 10:00
@Author  : Alexander Tomelo
"""
from datetime import datetime

import pytest
from tests.ReTests.GoogleSheets.googlesheets import GoogleSheet


@pytest.fixture(scope="class", autouse=True)
def gs():
    print(f"\n{datetime.now()}   *** start fixture gs = ... ***\n")
    """Start execution program"""
    # end_row = 1000
    # gs = GoogleSheet()
    # # проверка и получение данных ретеста
    # values = get_gs_data(end_row)

    # добавление нового столбца для результатов ретеста
    gs = GoogleSheet()
    gs.add_new_column_after_()

    # старт ретеста
    start_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    gs_out = ["'=====> Bugs Report !!! Идет Retest <====="]
    gs.update_range_values('B1', [gs_out])
    gs.update_range_values('V1', [start_retest_date])

    yield gs

    # окончание ретеста
    end_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    gs_out = ['Bugs Report']
    gs.update_range_values('B1', [gs_out])
    gs.update_range_values('V2', [end_retest_date])
    # exit(0)

    print(f"\n{datetime.now()}   *** end fixture gs = teardown ***\n")
