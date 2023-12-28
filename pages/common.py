"""
-*- coding: utf-8 -*-
@Time    : 2023/09/09 12:00
@Author  : Alexander Tomelo
"""
import sys
from datetime import datetime
from random import randint
import pytest
from conf import QTY_LINKS


class Common:

	def check_language_in_list_and_skip_if_present(self, cur_language, list_languages):
		if cur_language in list_languages:
			pytest.skip(f"This test is not for '{cur_language}' language")
		return

	def check_language_in_list_and_skip_if_not_present(self, cur_language, list_languages):
		if cur_language not in list_languages:
			pytest.skip(f"This test is not for '{cur_language}' language")
		return

	def check_country_in_list_and_skip_if_present(self, cur_country, list_countries):
		if cur_country in list_countries:
			pytest.skip(f"This test is not for '{cur_country}' country")
		return

	def check_country_in_list_and_skip_if_not_present(self, cur_country, list_countries):
		if cur_country not in list_countries:
			pytest.skip(f"This test is not for '{cur_country}' country")
		return

	def skip_test_for_language(self, cur_language) -> None:
		pytest.skip(f"This test-case is not for {cur_language} language")

	def skip_test_for_country(self, cur_country):
		pytest.skip(f"This test-case is not for {cur_country} country")

	def creating_file_of_hrefs(self, title_us, list_items, file_name, first_index=1):
		file = None
		list_url_out = list()

		print(f"{datetime.now()}")
		print(f"{datetime.now()}   {title_us} include {len(list_items) - first_index} child items for random select")

		count_in = len(list_items) - first_index  # иссключаем первую (родительскую) страницу, если first_index = 1
		count_out = 0
		url_prev = ""
		if count_in > 0:
			for i in range(QTY_LINKS):
				if i < count_in:
					while True:
						k = randint(first_index, count_in - 1)
						item = list_items[k]
						url = item.get_property("href")
						print(f"{datetime.now()}   k = {k} - {url}")
						if url != url_prev and url not in list_url_out:
							break
					list_url_out.append(url)
					url_prev = url
					count_out += 1

		try:
			file = open(file_name, "w")
			print(f"{datetime.now()}   The file of hrefs contains the following URLs:")
			for i in range(len(list_url_out)):
				url = list_url_out[i]
				file.write(url + "\n")
				print(f"{datetime.now()}   {url}")
		finally:
			file.close()
			del file

		print(f"{datetime.now()}   Test data include {count_out} item(s)")
		if count_in != 0:
			print(f"{datetime.now()}   The test coverage = {count_out / count_in * 100} %")
		else:
			print(f"{datetime.now()}   The test coverage = 0 %")

	def generate_cur_item_link_parameter(self, file_name):

		list_item_link = list()
		try:
			# проверка аргументов командной строки
			retest = sys.argv[1].split('=')[1]
		except IndexError:
			retest = False
		if retest == 'True':
			if sys.argv[6].split('=')[0] == "--tpi_link":
				list_item_link.append(sys.argv[6].split('=')[1])
		else:

			try:
				file = open(file_name, "r")
			except FileNotFoundError:
				print(f"{datetime.now()}   There is no file with name {file_name}!")
			else:
				for line in file:
					list_item_link.append(line[:-1])
					# print(f"{datetime.now()}   {line[:-1]}")
				file.close()

			qty = len(list_item_link)
			if qty == 0:
				print(f"{datetime.now()}   Отсутствуют тестовые данные: нет списка ссылок на страницы")
				sys.exit(1)
			else:
				print(f"{datetime.now()}   List of hrefs contains {qty} URLs")

		return list_item_link
