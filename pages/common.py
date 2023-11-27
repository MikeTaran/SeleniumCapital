"""
-*- coding: utf-8 -*-
@Time    : 2023/09/09 12:00
@Author  : Alexander Tomelo
"""
import pytest


class Common:

	def skip_test_for_language(self, cur_language) -> None:
		pytest.skip(f"This test-case is not for {cur_language} language")

	def skip_test_for_country(self, cur_country):
		pytest.skip(f"This test-case is not for {cur_country} country")
