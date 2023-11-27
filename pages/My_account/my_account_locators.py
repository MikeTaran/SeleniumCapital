"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
from selenium.webdriver.common.by import By


class MyAccountLocator:
    """ Locators for ..."""
    LOGOUT = (By.CSS_SELECTOR, "#userPanel div.logout-user")
    TRADING_PLATFORM = (By.CSS_SELECTOR, "#userPanel button.tradingPlatformBtn")
    CLOSE = (By.CSS_SELECTOR, "#userPanel span.user-panel-close")
    USER_LOGIN = (By.CSS_SELECTOR, "#userPanel div.user-login")
