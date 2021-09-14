from pages_go.GooglePageGo import GooglePageGo
import allure


class TestAuthorization:

    @allure.title('Запуск:авторизация с неверным паролем и логиным')
    @allure.severity('CRITICAL')
    def test_authorization_with_a_non_existent_password_and_username(self, web_driver):
        mainestimatepage = GooglePageGo(web_driver)
        mainestimatepage.go_to_base_url()
        mainestimatepage.check_text_element_attribute(mainestimatepage.text_for_button, mainestimatepage.button_my_lucky)
        mainestimatepage.check_url(mainestimatepage.base_url)
        mainestimatepage.entering_text(mainestimatepage.text_for_test, mainestimatepage.input_search)
        mainestimatepage.check_text_element(mainestimatepage.text_for_test, mainestimatepage.text_in_input_search)
