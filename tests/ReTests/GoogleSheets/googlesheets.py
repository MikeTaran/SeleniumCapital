"""
-*- coding: utf-8 -*-
@Time    : 18/12/2023
@Author  : Mike Taran
"""

import os.path
from datetime import datetime

import allure
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheet:
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    # RANGE_NAME = "BugsReport!A4:P4"
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    # The ID and range of a spreadsheet.
    SPREADSHEET_ID = "1jG0hdjrUdjMFBYHXyBKRGbBwV0ICxfBPaBkgB98Nuuk"
    # SPREADSHEET_ID = "1qpqNe8ZA6ypGbJh0uqRDIFJMtzaRARCOIVyoCuBXWz4"     # copy for debugging
    SHEET_NAME = 'BugsReport'
    SHEET_ID = '540090404'
    service = None

    def __init__(self):
        creds = None
        if os.path.exists("./tests/ReTests/token.json"):
            creds = Credentials.from_authorized_user_file("./tests/ReTests/token.json", self.SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    "./tests/ReTests/credentials.json", self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open("./tests/ReTests/token.json", "w") as token:
                token.write(creds.to_json())

        try:
            self.service = build("sheets", "v4", credentials=creds)
        except HttpError as err:
            print(err)

    # Этот будет принимать имя листа и идентификатор таблицы, затем находить и возвращать
    # идентификатор листа по его имени.
    def get_sheet_id(self, sheet_name, spreadsheet_id):
        sheet_metadata = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        sheets = sheet_metadata.get('sheets', '')
        for sheet in sheets:
            if sheet['properties']['title'] == sheet_name:
                return sheet['properties']['sheetId']
        return None  # Если лист не найден

    def add_new_column_after_(self, index_of_col=22):
        print(f"\n{datetime.now()}   Добавление нового столбца =>")
        if index_of_col is not None:
            request_body = {
                'requests': [{
                    'insertDimension': {
                        'range': {
                            'sheetId': self.SHEET_ID,
                            'dimension': 'COLUMNS',
                            'startIndex': index_of_col,
                            'endIndex': index_of_col + 1  # Вставляем сразу после столбца 'V'
                        }
                    }
                }]
            }
            self.service.spreadsheets().batchUpdate(spreadsheetId=self.SPREADSHEET_ID,
                                                    body=request_body).execute()
        else:
            print(f"Столбец {index_of_col} не найден в таблице.")

        print(f"\n{datetime.now()}   => Новый столбец добавлен")

    def add_new_row_after_(self, index_of_row=3):
        print(f"\n{datetime.now()}   Добавление новой строки =>")
        if index_of_row is not None:
            request_body = {
                'requests': [{
                    'insertDimension': {
                        'range': {
                            'sheetId': self.SHEET_ID,
                            'dimension': 'ROWS',
                            'startIndex': index_of_row,
                            'endIndex': index_of_row + 1  # Вставляем сразу после строки 3
                        }
                    }
                }]
            }
            self.service.spreadsheets().batchUpdate(spreadsheetId=self.SPREADSHEET_ID,
                                                    body=request_body).execute()
        else:
            print(f"Строка {index_of_row} не найдена в таблице.")

        print(f"\n{datetime.now()}   => Новая строка добавлена")

    def add_new_row_before_(self, index_of_row=5):
        print(f"\n{datetime.now()}   Добавление новой строки =>")
        if index_of_row is not None:
            request_body = {
                'requests': [{
                    'insertDimension': {
                        'range': {
                            'sheetId': self.SHEET_ID,
                            'dimension': 'ROWS',
                            'startIndex': index_of_row - 1,
                            'endIndex': index_of_row  # Вставляем перед строкой 5
                        }
                    }
                }]
            }
            self.service.spreadsheets().batchUpdate(spreadsheetId=self.SPREADSHEET_ID,
                                                    body=request_body).execute()
        else:
            print(f"Строка {index_of_row} не найдена в таблице.")

        print(f"\n{datetime.now()}   => Новая строка добавлена")

    @allure.step("Get row values from ... row")
    def get_row_values(self, end_row=5):
        print(f"\n{datetime.now()}   1. get_row_values from {end_row} row =>")
        range_name = f"{self.SHEET_NAME}!A{end_row}:P{end_row}"
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=self.SPREADSHEET_ID, range=range_name)
            .execute()
        )
        values = result.get("values", [])
        print(f"{datetime.now()}   => row values = \n{values}")
        print(f"\n{datetime.now()}   => 1. Get row values from {end_row} row finished")

        return values

    def get_all_row_values(self, start_row=5):
        range_name = f"{self.SHEET_NAME}!A{start_row}:P"
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=self.SPREADSHEET_ID, range=range_name)
            .execute()
        )
        values = result.get("values", [])

        return values

    def get_cell_values(self, cell):
        cell_range_name = f"{self.SHEET_NAME}!{cell}"
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=self.SPREADSHEET_ID, range=cell_range_name)
            .execute()
        )
        values = result.get("values", [])

        return values

    @allure.step("Fixing one row check results into Google Sheet Bugs Report")
    def update_range_values(self, cell='V5', values=""):
        if values == "":
            values = [[""]]
        print(f"\n{datetime.now()}   4. Fixing one row check results into Google Sheet Bugs Report =>")
        range_name = f'{self.SHEET_NAME}!{cell}'
        data = [{
            'range': range_name,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID,
                                                                  body=body).execute()
        print('{0} cells updated.'.format(result.get('totalUpdatedCells')))
        print(f"{datetime.now()}   => 4. One row check results into Google Sheet Bugs Report fixed")

        return result

    def new_data_copy_past(self, source_startRowIndex=5, source_endRowIndex=6,
                           destination_startRowIndex=4, destination_endRowIndex=5,
                           source_startColumnIndex=0, source_endColumnIndex=17,
                           destination_startColumnIndex=0, destination_endColumnIndex=17):
        sheet = self.service.spreadsheets()

        # Копирование формул и форматирования из предыдущей строки
        copy_request = {
            "requests": [
                {
                    "copyPaste": {
                        "source": {
                            "sheetId": self.SHEET_ID,
                            "startRowIndex": source_startRowIndex,
                            "endRowIndex": source_endRowIndex,  # end-start=количество строк
                            "startColumnIndex": source_startColumnIndex,
                            "endColumnIndex": source_endColumnIndex  # end-start=количество столбцов
                        },
                        "destination": {
                            "sheetId": self.SHEET_ID,
                            "startRowIndex": destination_startRowIndex,
                            "endRowIndex": destination_endRowIndex,  # end-start=количество строк
                            "startColumnIndex": destination_startColumnIndex,
                            "endColumnIndex": destination_endColumnIndex  # end-start=количество столбцов
                        },
                        "pasteType": "PASTE_NORMAL"  # Копирование формул
                    }
                }
            ]
        }

        response = sheet.batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=copy_request).execute()

    def new_column_copy_past(self, source_column=22, destination_column=23):
        pass

    def clear_values_new_column(self, column=22):
        pass

    def clear_values(self, range_startRowIndex=1, range_endRowIndex=1, range_startColumnIndex=1,
                     range_endColumnIndex=1):
        sheet = self.service.spreadsheets()

        # Очистка значений в новой строке
        clear_request = {
            "requests": [
                {
                    "updateCells": {
                        "range": {
                            "sheetId": self.SHEET_ID,
                            "startRowIndex": range_startRowIndex,
                            "endRowIndex": range_endRowIndex,
                            "startColumnIndex": range_startColumnIndex,
                            "endColumnIndex": range_endColumnIndex
                        },
                        "fields": "userEnteredValue"  # Очистка только значений
                    }
                }
            ]
        }

        response = sheet.batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=clear_request).execute()

    def date_format_cell(self):
        sheet = self.service.spreadsheets()
        date_format_request = {
            "requests": [
                {
                    "repeatCell": {
                        "range": {
                            "sheetId": self.SHEET_ID,
                            "startRowIndex": 2,
                            "endRowIndex": 3,
                            "startColumnIndex": 22,
                            "endColumnIndex": 23
                        },
                        "cell": {
                            "userEnteredFormat": {
                                "numberFormat": {
                                    "type": "DATE",
                                    "pattern": "dd/mm/yyyy"  # Формат даты W3
                                }
                            }
                        },
                        "fields": "userEnteredFormat.numberFormat"
                    }
                }
            ]
        }

        response = sheet.batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=date_format_request).execute()
