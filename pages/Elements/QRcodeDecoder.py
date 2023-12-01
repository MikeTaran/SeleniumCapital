"""
-*- coding: utf-8 -*-
@Time    : 2023/04/20 22:00
@Author  : Suleyman Alirzaev
"""
# import time
from datetime import datetime
import pytest
import allure

from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import QRCodeLocators
# from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# import cv2
# from pyzbar import pyzbar
# import zxing
# from qreader import QReader

# import os
# import aspose.barcode as barcode
# import urllib.request


class QRCodeDecode(BasePage):

    def __init__(self, browser, link, qr_code):
        super().__init__(browser, link)
        self.element = None
        self.locator_link = None
        self.locator = None
        self.qr_code = qr_code

    def arrange(self):
        print(f"\n{datetime.now()}   1. Arrange")
        print(f"\n{datetime.now()}   Testing the qr code: {self.qr_code.upper()}")
        if not self.current_page_is(self.link):
            self.open_page()
        match self.qr_code:
            case 'investmate':
                locator = QRCodeLocators.QR_CODE_INVESTMATE
                locator_link = QRCodeLocators.QR_CODE_INVESTMATE_LINK
            case 'easy_learning':
                locator = QRCodeLocators.QR_CODE_EASY_LEARNING
                locator_link = QRCodeLocators.QR_CODE_EASY_LEARNING_LINK
            case _:
                locator = QRCodeLocators.QR_CODE_CAPITAL
                locator_link = QRCodeLocators.QR_CODE_CAPITAL_LINK

        print(f"{datetime.now()}   QR_CODE is visible? =>")

        if self.element_is_visible(locator, 30):
            print(f"{datetime.now()}   => QR_CODE_{self.qr_code.upper()} is visible on the page!")
        else:
            print(f"{datetime.now()}   => QR_CODE_{self.qr_code.upper()} is not visible on the page!")

        print(f"{datetime.now()}   QR_CODE_LINK is present on the page? =>")
        self.element = self.element_is_visible(locator_link, 30)
        if self.element:
            print(f"{datetime.now()}   => QR_CODE_LINK {self.qr_code.upper()} is on the page!")
            return self
        else:
            print(f"{datetime.now()}   => QR_CODE_LINK {self.qr_code.upper()} is not on the page!")
            pytest.fail(f"Checking element QR_CODE_LINK {self.qr_code.upper()} is not on the page")

    @allure.step("Determining the qr code link")
    def element_decode(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Determining the QR_CODE link")
        qr_link = self.element.get_attribute('title')
        if qr_link:
            print(f"{datetime.now()}   QR_CODE link: {qr_link}")
            self.link = qr_link
            self.open_page()
        else:
            pytest.fail("QR_CODE_LINK IS NOT DEFINED")

        # print(f"\n{datetime.now()}   2. Act")
        # print(f"{datetime.now()}   QR_CODE_{self.filename.upper()} is present? =>")
        # code_list = self.browser.find_elements(*self.locator_link)
        # if len(code_list) == 0:x
        #     print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} is not present on the page!")
        #     return False
        # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} is present on the page!")
        #
        # print(f"{datetime.now()}   QR_CODE_{self.filename.upper()} scroll =>")
        #
        # self.browser.execute_script(
        #     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #     code_list[0]
        # )

        # try:
            # qr_code_locator = self.browser.find_element(*self.locator)
            # link = qr_code_locator.get_attribute
            # link = self.get_attribute("title", *self.locator_link)
            # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} found")
            # print(f"{datetime.now()}   => Opening link from QR_CODE")
            # self.link = link
            # self.open_page()
            # self.browser.get(link)
            # self.wait_for_target_url('apps.apple.com', 10)

            # time.sleep(5)
            # ########### Не удалять ############
            # qr_code = self.browser.find_element(*self.locator)
            # src = qr_code.get_attribute('src')
            # # Download the image
            # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} download started.")
            # urllib.request.urlretrieve(src, f"test_data/{self.filename}.png")
            # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} downloaded.")
            # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} scanning started.")
            #
            # # Load QR code image
            # reader = barcode.barcoderecognition.BarCodeReader(f"test_data/{self.filename}.png")
            #
            # # Read QR codes
            # recognized_results = reader.read_bar_codes()
            #
            # for x in recognized_results:
            #     url_end = x.code_text.find(" ")
            #     url_2 = x.code_text[0:url_end]
            # self.browser.get(url_2)
            # os.remove(f"test_data/{self.filename}.png")

            # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} scanned!")
            ####################################
        # except ElementClickInterceptedException:
        #     print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} NOT CLICKED")
        #
        # return True
