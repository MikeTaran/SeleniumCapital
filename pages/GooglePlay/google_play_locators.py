from selenium.webdriver.common.by import By


class GooglePlayLocators:
	APP_TITLE = (By.CSS_SELECTOR, "h1[itemprop='name'] span")
	PROVIDER = (By.CSS_SELECTOR, "a[href^='/store/apps/dev?'] span")
