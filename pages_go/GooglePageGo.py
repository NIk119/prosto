from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pages.GooglePage import GooglePage
import allure
import time


class GooglePageGo(GooglePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.button_my_lucky: str = (By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@value='Поиск в Google']")
        self.input_search: str = (By.XPATH, "//input[@class='gLFyf gsfi']")
        self.text_in_input_search: str = (By.XPATH, "//div[@class='pR49Ae gsfi']/span")

    @allure.step("Ввод текста")
    def entering_text(self, login: str, locator: str) -> None:
        element = self.wait_element(locator)
        element.click()
        element.clear()
        element.send_keys(login)

