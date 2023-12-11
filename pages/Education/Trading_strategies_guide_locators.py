"""
-*- coding: utf-8 -*-
@Time    : 2023/09/30 21:33
@Author  : Mila Podchasova
"""
from selenium.webdriver.common.by import By


class TradingStrategiesContentList:
    LISTS = (By.CSS_SELECTOR, "div.markets-list > div.item a.h3")
