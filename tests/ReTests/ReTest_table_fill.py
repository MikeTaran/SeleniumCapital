from datetime import datetime
from tests.ReTests.GoogleSheets.googlesheets import GoogleSheet


def check_gs_table(bid, bug_n):
    gs = GoogleSheet()
    # старт проверки
    gs_out = ["'=====> Bugs Report !!! Идет Retest Data Update <====="]
    gs.update_range_values('B1', [gs_out])

    available = True
    gs = GoogleSheet()
    values = gs.get_all_row_values()
    for index, row in enumerate(values):
        if not row:
            break
        else:
            if bid in row[0]:
                if bug_n in row[-1]:
                    available = False
                    return available
                else:
                    bug_num = [["'" + bug_n]]
                    gs.update_range_values(f'P{5 + index}', bug_num)
                    print(f"\n{datetime.now()}   Bug: {bid} уже существует, "
                          f"но тип бага изменился с {row[-1]} на {bug_n}")
                    available = False
                    return available
    return available


def new_row_data(bid, bug_num, link):
    # bid = "Bid:11.01.01.00_01-de.ae.NoReg"
    us = bid.split(':')[1].split('-')[0].split('_')[0]
    tc = '_' + bid.split(':')[1].split('-')[0].split('_')[1]
    lng = bid.split(':')[1].split('-')[1].split('.')[0]
    ctr = bid.split(':')[1].split('-')[1].split('.')[1]
    rol = bid.split(':')[1].split('-')[1].split('.')[2]
    if us.split('.')[-1] == '00':
        link = ""

    new_bug_data_1 = [[bid, 'Ubuntu 22.04', 'Chrome', us, tc, lng, ctr]]
    new_bug_data_2 = [[rol, link]]
    return new_bug_data_1, new_bug_data_2


def add_new_row_with_format():
    gs = GoogleSheet()

    start_update_date = [datetime.now().strftime("%d/%m/%y")]
    # добавление новой 4-й строки
    gs.add_new_row_before_()
    # копирование данных из предыдущей строки
    gs.new_data_copy_past(5, 6, 4, 5,
                          0, 17, 0, 17)
    # gs.clear_values_new_row()
    gs.update_range_values('U5', [start_update_date])


def fill_gs_table(value_1, value_2, bug_num):
    gs = GoogleSheet()
    gs.update_range_values('A5', value_1)
    gs.update_range_values('I5', value_2)
    gs.update_range_values('P5', [[bug_num]])


def retest_table_fill(bid="", bug_n="", link=""):
    # ========= не удалять ======================
    # bid = "Bid:11.02.02.01_07-en.de.Auth"
    # bug_n = "05"
    # link = 'https://capital.com/pl/handlovac-amd'
    # ===========================================

    print(f"\n{datetime.now()}   Проверка бага в таблице ретеста  =>")
    gs = GoogleSheet()
    if bid != "":
        bug_num = "'" + bug_n

        # проверка таблицы багов
        available = check_gs_table(bid, bug_n)
        if available:

            # формирование данных для заполнения
            new_bug_data_1, new_bug_data_2 = new_row_data(bid, bug_num, link)

            # добавление новой строки с копипастом формул и форматов
            add_new_row_with_format()

            # заполнение таблицы
            fill_gs_table(new_bug_data_1, new_bug_data_2, bug_num)

            print(f"\n{datetime.now()}   Bug: {bid}-{bug_n} добавлен в таблицу для ретеста")

        else:
            print(f"\n{datetime.now()}   Bug: {bid}-{bug_n} уже существует")
    else:
        print(f"\n{datetime.now()}  Для бага: Bid-{bug_n} необходимо использовать проверку на ретест!!!")

    gs_out = ['Bugs Report']
    gs.update_range_values('B1', [gs_out])


# # ========= не удалять ======================
# if __name__ == "__main__":
#     retest_table_fill()
