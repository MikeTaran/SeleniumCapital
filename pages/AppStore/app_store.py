"""
-*- coding: utf-8 -*-
@Time    : 2023/06/20 11:00
@Author  : Andrey Bozhko
"""
import allure
from datetime import datetime
from pages.base_page import BasePage
from pages.AppStore.app_store_locators import AppStoreLocators
from test_data.app_store_data import data, data_investmate


class AppStore(BasePage):
    @allure.step("Checking that the App Store page has opened")
    def should_be_app_store_page(self, cur_link):
        """Check if the page is open"""
        print(f"{datetime.now()}   Checking that the App Store page has opened")
        self.wait_for_change_url(cur_link, 10)
        if self.current_page_url_contain_the(data["APP_URL"]):
            self.should_be_page_title_v2(data["PAGE_TITLE"])
            self.should_be_app_store_app_title(data["APP_TITLE"])
            self.should_be_app_store_specifies_provider(data["PROVIDER"])
            self.open_page()
            assert True
        else:
            self.open_page()
            assert False, f'Loaded page with not {data["APP_URL"]} url. Current URL is {self.browser.current_url}'

    @allure.step("Checking that the App Store Investmate page has opened")
    def should_be_app_store_investmane_page(self):
        """Check if the page is open"""
        print(f"{datetime.now()}   Checking that the App Store page has opened")
        # self.wait_for_change_url(cur_link, 10)
        if self.current_page_url_contain_the(data_investmate["APP_URL"]):
            self.should_be_page_title_v2(data_investmate["PAGE_TITLE"])
            self.should_be_app_store_app_title(data_investmate["APP_TITLE"])
            self.should_be_app_store_specifies_provider(data_investmate["PROVIDER"])
            self.open_page()
            assert True
        else:
            self.open_page()
            assert False, (f'Loaded page with not {data_investmate["APP_URL"]} url. '
                           f'Current URL is {self.browser.current_url}')

    @allure.step("Checking that the App Store app title")
    def should_be_app_store_app_title(self, app_title):
        """Check if the app title"""
        print(f"{datetime.now()}   Checking that the App Store app title")
        assert self.get_text(0, *AppStoreLocators.APP_TITLE) == app_title

    @allure.step("Checking that the App Store specifies provider")
    def should_be_app_store_specifies_provider(self, provider):
        """Check if the specifies provider"""
        print(f"{datetime.now()}   Checking that the App Store specifies provider")
        assert self.get_text(0, *AppStoreLocators.PROVIDER) == provider
