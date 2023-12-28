"""
-*- coding: utf-8 -*-
@Time    : 18/12/2023
@Author  : Mike Taran
"""

import os.path
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheet:
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    RANGE_NAME = "BugsReport!A4:P4"
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    # The ID and range of a spreadsheet.
    SPREADSHEET_ID = "1jG0hdjrUdjMFBYHXyBKRGbBwV0ICxfBPaBkgB98Nuuk"
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

    def add_new_column_after_(self, index_of_col=21):
        print(f"\n{datetime.now()}   Добавление нового столбца =>")
        if index_of_col is not None:
            request_body = {
                'requests': [{
                    'insertDimension': {
                        'range': {
                            'sheetId': self.SHEET_ID,
                            'dimension': 'COLUMNS',
                            'startIndex': index_of_col,
                            'endIndex': index_of_col + 1  # Вставляем сразу после столбца 'R'
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

    def get_row_values(self, end_row=4):
        range_name = f"{self.SHEET_NAME}!A{end_row}:P{end_row}"
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=self.SPREADSHEET_ID, range=range_name)
            .execute()
        )
        values = result.get("values", [])

        return values

    def get_all_row_values(self, end_row=4):
        range_name = f"{self.SHEET_NAME}!A{end_row}:P"
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

    def update_range_values(self, cell='V4', values=""):
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
        return result

    def new_row_copy_past(self, source_row=5, destination_row=4):
        sheet = self. service.spreadsheets()

        # Копирование формул и форматирования из предыдущей строки
        copy_request = {
            "requests": [
                {
                    "copyPaste": {
                        "source": {
                            "sheetId": self.SHEET_ID,
                            "startRowIndex": source_row-1,
                            "endRowIndex": source_row,
                            "startColumnIndex": 0,
                            "endColumnIndex": 17  # количество столбцов (A:Q)
                        },
                        "destination": {
                            "sheetId": self.SHEET_ID,
                            "startRowIndex": destination_row-1,
                            "endRowIndex": destination_row,
                            "startColumnIndex": 0,
                            "endColumnIndex": 17    # количество столбцов (A:Q)
                        },
                        "pasteType": "PASTE_NORMAL"  # Копирование формул
                    }
                }
            ]
        }

        response = sheet.batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=copy_request).execute()

    def clear_values_new_row(self, row=4):
        sheet = self.service.spreadsheets()

        # Очистка значений в новой строке
        clear_request = {
            "requests": [
                {
                    "updateCells": {
                        "range": {
                            "sheetId": self.SHEET_ID,
                            "startRowIndex": row - 1,
                            "endRowIndex": row,
                            "startColumnIndex": 0,
                            "endColumnIndex": 16  # количество столбцов (A:P)
                        },
                        "fields": "userEnteredValue"  # Очистка только значений
                    }
                }
            ]
        }

        response = sheet.batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=clear_request).execute()
