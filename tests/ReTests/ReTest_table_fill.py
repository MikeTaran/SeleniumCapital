from datetime import datetime
from tests.ReTests.GoogleSheets.googlesheets import GoogleSheet


def check_gs_table(bid, bug_num):
    gs = GoogleSheet()
    # старт проверки
    gs_out = ["'=====> Bugs Report !!! Идет Retest Data Update <====="]
    gs.update_range_values('B1', [gs_out])

    available = True
    gs = GoogleSheet()
    values = gs.get_all_row_values()
    for row in values:
        if not row:
            break
        else:
            if bid in row[0]:
                if bug_num in row[-1]:
                    available = False
                    return available
    return available


def new_row_data(bid, bug_num, link):
    # bid = "Bid:11.01.01.00_01-de_ae_NoReg"
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
    gs.add_new_row_after_()
    gs.new_row_copy_past()
    # gs.clear_values_new_row()
    gs.update_range_values('U4', [start_update_date])


def fill_gs_table(value_1, value_2, bug_num):
    gs = GoogleSheet()
    gs.update_range_values('A4', value_1)
    gs.update_range_values('I4', value_2)
    gs.update_range_values('P4', [[bug_num]])


def retest_table_fill(bid="", bug_n="", link=""):
    # ========= не удалять ======================
    # bid = "Bid:11.01.01.00_01-de_ae_NoReg"
    # bug_n = "05"
    # link = 'https://capital.com/pl/handlovac-amd'
    # ===========================================

    print(f"\n{datetime.now()}   Проверка бага в таблице ретеста  =>")
    bug_num = "'" + bug_n
    gs = GoogleSheet()

    # проверка таблицы багов
    available = check_gs_table(bid, bug_n)
    if available:

        # формирование данных для заполнения
        new_bug_data_1, new_bug_data_2 = new_row_data(bid, bug_num, link)

        # добавление новой строки с копипастом формул и форматов
        add_new_row_with_format()

        # заполнение таблицы
        fill_gs_table(new_bug_data_1, new_bug_data_2, bug_num)

        print(f"\n{datetime.now()}   Bug: {bid}-{bug_num} добавлен в таблицу для ретеста")

    else:
        print(f"\n{datetime.now()}   Bug: {bid}-{bug_n} уже существует")

    gs_out = ['Bugs Report']
    gs.update_range_values('B1', [gs_out])

# # ========= не удалять ======================
# if __name__ == "__main__":
#     retest_table_fill()
