"""
-*- coding: utf-8 -*-
@Time    : 2023/12/24 10:00
@Author  : Alexander Tomelo
"""
import pytest
from tests.ReTests.GoogleSheets.googlesheets import GoogleSheet
from tests.ReTests.ReTests import unique_test, retest_skipped_tests, no_new_column
from datetime import datetime, timedelta


def time_concat(time1, time2):

    # Преобразование строк в объекты времени
    time1_obj = datetime.strptime(time1, "%H:%M:%S")
    time2_obj = datetime.strptime(time2, "%H:%M:%S")

    # Сложение временных объектов
    result_time_obj = time1_obj + timedelta(hours=time2_obj.hour, minutes=time2_obj.minute, seconds=time2_obj.second)

    # Преобразование результата обратно в строку
    result_time_str = result_time_obj.strftime("%H:%M:%S")

    return result_time_str


@pytest.fixture(
    scope="session"
    # , autouse=True
)
def gs():
    print(f"\n{datetime.now()}   *** start fixture gs = ... ***\n")
    """Start execution program"""

    gs = GoogleSheet()
    # получение длины таблицы
    values = gs.get_all_row_values()
    rows_qty = len(values)
    execution_time_1 = gs.get_row_values(4)[0][21]
    del values

    # старт ретеста
    start_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    gs_out = ["'=====> Bugs Report !!! Идет Retest <====="]
    gs.update_range_values('B1', [gs_out])

    if unique_test or retest_skipped_tests or no_new_column:
        # установка времени старта ретеста
        gs.update_range_values('V1', [start_retest_date])
        # установка таймера выполнения ретестов
        # # для запуска на Github
        # gs.update_range_values('V4', [["=NOW()-V1-TIME(3;0;0)"]])
        # для запуска на локальном компе
        gs.update_range_values('V4', [["=NOW()-V1-TIME(1;0;0)"]])
        # установка счетчика пройденных тестов
        gs.new_data_copy_past(1, 2, 1, 2,
                              0, 1, 21, 22)

    else:

        # # добавление нового столбца для результатов ретеста
        gs.add_new_column_after_()
        #
        # # копирование данных столбца
        gs.new_data_copy_past(0, rows_qty, 0, rows_qty,
                              21, 22, 22, 23)
        #
        # # очистка полей
        gs.clear_values(4, rows_qty, 21, 22)
        #
        # # замена значения Status на дату ретеста
        gs.update_range_values('W3', [["=W2"]])
        gs.date_format_cell()

        # установка времени старта ретеста
        gs.update_range_values('V1', [start_retest_date])

        # установка таймера выполнения ретестов
        # # для запуска на Github
        gs.update_range_values('V4', [["=NOW()-V1-TIME(3;0;0)"]])

        # для запуска на локальном компе
        # gs.update_range_values('V4', [["=NOW()-V1"]])

        # установка счетчика пройденных тестов
        gs.new_data_copy_past(1, 2, 1, 2,
                              0, 1, 21, 22)

    yield gs

    # окончание ретеста

    gs_out = ['Bugs Report']
    gs.update_range_values('B1', [gs_out])

    if unique_test or retest_skipped_tests or no_new_column:
        end_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
        gs.update_range_values('V2', [end_retest_date])
        execution_time_2 = gs.get_row_values(4)[0][21]
        # установка полного времени тестирования
        execution_time = time_concat(execution_time_1, execution_time_2)
        gs.update_range_values('V4', [[execution_time]])

    else:
        end_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
        gs.update_range_values('V2', [end_retest_date])
        gs.update_range_values('V4', [["=V2 - V1"]])

    print(f"\n{datetime.now()}   *** end fixture gs = teardown ***\n")
