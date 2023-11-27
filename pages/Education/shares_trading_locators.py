"""
-*- coding: utf-8 -*-
@Time    : 2023/09/01 13:55
@Author  : Azarov Pavel
"""
from selenium.webdriver.common.by import By


class SharesTradingItem:
    ITEM_LIST = (By.CSS_SELECTOR, "div.side-nav > a")
