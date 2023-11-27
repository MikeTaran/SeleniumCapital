from selenium.webdriver.common.by import By


class AppStoreLocators:
	APP_TITLE = (By.CSS_SELECTOR, "h1")
	PROVIDER = (By.CSS_SELECTOR, "h2.app-header__identity")
