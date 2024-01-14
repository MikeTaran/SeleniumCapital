"""
-*- coding: utf-8 -*-
@Time    : 2023/12/24 10:00
@Author  : Alexander Tomelo
"""
from datetime import datetime

import pytest
from tests.ReTests.GoogleSheets.googlesheets import GoogleSheet


@pytest.fixture(
    scope="class"
    # , autouse=True
)
def gs():
    print(f"\n{datetime.now()}   *** start fixture gs = ... ***\n")
    """Start execution program"""

    gs = GoogleSheet()
    # получение длины таблицы
    values = gs.get_all_row_values()
    rows_qty = len(values)
    del values

    # старт ретеста
    start_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    gs_out = ["'=====> Bugs Report !!! Идет Retest <====="]
    gs.update_range_values('B1', [gs_out])

    # добавление нового столбца для результатов ретеста
    gs.add_new_column_after_()

    # копирование данных столбца
    gs.new_data_copy_past(0, rows_qty, 0, rows_qty,
                          21, 22, 22, 23)

    # замена значения Status на дату ретеста
    gs.update_range_values('W3', [["=W2"]])
    gs.date_format_cell()

    # установка времени старта ретеста
    gs.update_range_values('V1', [start_retest_date])

    # установка таймера выполнения ретестов
    gs.update_range_values('V4', [["=NOW()-V1-TIME(3;0;0)"]])

    # установка счетчика пройденных тестов
    gs.new_data_copy_past(1, 2, 1, 2,
                          0, 1, 21, 22)

    # очистка полей
    gs.clear_values(4, rows_qty, 21, 22)

    yield gs

    # окончание ретеста
    end_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    gs_out = ['Bugs Report']
    gs.update_range_values('V2', [end_retest_date])
    gs.update_range_values('V4', [["=V2 - V1"]])
    gs.update_range_values('B1', [gs_out])
    # exit(0)

    print(f"\n{datetime.now()}   *** end fixture gs = teardown ***\n")
