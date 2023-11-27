"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
from selenium.webdriver.common.by import By


class FinancialDictionary:
    ALPHABET_LIST = (By.CSS_SELECTOR,
                     "glossaryWrapper > div.alphabet-list-container > div > div > span.alphabet-list-item")
    ITEM_LIST = (By.CSS_SELECTOR, "div.alphabet-category-item > div.inner a")
