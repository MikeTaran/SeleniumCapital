"""
-*- coding: utf-8 -*-
@Time    : 2023/07/17 07:00
@Author  : Alexander Tomelo
"""
from datetime import datetime

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Captcha(BasePage):

    CAPTCHA_API_KEY = "8729f4a5a40472cb058438731884ded9"
    LOCATOR = "div.g-recaptcha[data-sitekey]"

    @allure.step("Start Checking Captcha")
    def is_captcha_v2(self, driver):
        captcha = driver.find_elements(By.CSS_SELECTOR, self.LOCATOR)
        if len(captcha) == 0:
            print(f"\n{datetime.now()}   Капчи нет. Тестим дальше")
            return False
        return True

    def print_env(self, driver):
        data_site_key = driver.find_elements(By.CSS_SELECTOR, self.LOCATOR)[0].get_property("data-sitekey")
        captcha_page_url = driver.current_url
        print(f"{datetime.now()}   На странице {captcha_page_url} проявилась Captcha")
        print(f"{datetime.now()}   SiteKey = {data_site_key}")
