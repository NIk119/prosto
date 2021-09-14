import ast
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class GooglePage():

    def __init__(self, web_driver):
        self.browser = web_driver
        self.base_url = "https://www.google.ru/"
        self.browser.implicitly_wait(5)
        self.browser.set_window_size(1720, 800)
        self.text_for_test: str = "sdf"
        self.text_for_button: str = "Поиск в Google"


    @allure.step("Зашли на сайт")
    def go_to_base_url(self) -> str:
        return self.browser.get(self.base_url)

    @allure.step("Ожидаем элемент")
    def wait_element(self, locator: str, time: int = 10) -> bool:
        try:
            return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator))
        except:
            return False

    @allure.step("Проверка url")
    def check_url(self, url: str, time: int = 10) -> bool:
        try:
            return WebDriverWait(self.browser, time).until(EC.url_matches(url))
        except TimeoutException:
            return False



    @allure.step(f"Проверка текста элемента")
    def check_text_element(self, text: str, locator: str, time: int = 10) -> bool:
        try:
            return WebDriverWait(self.browser, time).until(EC.text_to_be_present_in_element(locator, text), message=f"Текст отсутствует")
        except TimeoutException:
            return False


    @allure.step(f"Проверка текста элемента")
    def check_text_element_attribute(self, text: str, locator: str) -> bool:
        try:
            assert self.browser.find_element_by_xpath(locator[1]).get_attribute("value") == text, "Текст отсутствует"
            return True
        except:
            return False





