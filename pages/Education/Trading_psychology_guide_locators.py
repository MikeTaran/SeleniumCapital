"""
-*- coding: utf-8 -*-
@Time    : 2023/07/20 17:00
@Author  : Mila Podchasova
"""
from selenium.webdriver.common.by import By


class TradingPsychologyContentList:
    LISTS = (By.CSS_SELECTOR, "div.markets-list > div.item a.h3")
