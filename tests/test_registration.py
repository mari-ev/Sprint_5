import pytest
from pages.auth_page import AuthPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import AUTH_LOCATORS


class TestRegistration:
    def _click_element(self, locator_key):
        """Клик по элементу с ожиданием кликабельности."""
        element = self.wait.until(
            EC.element_to_be_clickable(AUTH_LOCATORS[locator_key])
        )
        element.click()

    def _fill_field(self, locator_key, text):
        """Заполнение поля с ожиданием возможности ввода."""
        field = self.wait.until(EC.element_to_be_clickable(AUTH_LOCATORS[locator_key]))
        field.send_keys(text)

    def _assert_element_displayed(self, locator_key, error_message):
        """Проверка видимости элемента."""
        element = self.wait.until(
            EC.presence_of_element_located(AUTH_LOCATORS[locator_key])
        )
        assert element.is_displayed(), error_message

    def _assert_text_in_element(self, locator_key, expected_text, error_template):
        """Проверка текста в элементе."""
        element = self.wait.until(
            EC.presence_of_element_located(AUTH_LOCATORS[locator_key])
        )
        actual_text = element.text.strip()
        assert expected_text in actual_text, error_template.format(
            actual_text=actual_text
        )

    @pytest.fixture
    def invalid_email(self):
        """Фикстура для генерации некорректного email."""
        return "test@"

    # Тест 1: Успешная регистрация нового пользователя
    def test_successful_registration(self, driver, wait, test_credentials):
        email, password = test_credentials
        auth_page = AuthPage(driver, wait)

        auth_page.open_page("https://qa-desk.stand.praktikum-services.ru/")
        auth_page.open_login_registration_modal()
        auth_page.switch_to_registration()
        auth_page.fill_email(email)
        auth_page.fill_password(password)
        auth_page.confirm_password(password)
        auth_page.submit_registration()
        auth_page.wait_for_modal_close()

        assert (
            auth_page.is_post_ad_button_displayed()
        ), "Кнопка «Разместить объявление» не отображается на главной странице"
        assert (
            auth_page.is_user_avatar_displayed()
        ), "Аватар-заглушка не отображается после регистрации"
        actual_name = auth_page.get_user_name()
        assert (
            "User" in actual_name
        ), f"Ожидалось, что имя пользователя будет содержать 'User', но найдено: '{actual_name}'"

    # Тест 2: Регистрация с email не по маске
    def test_registration_with_invalid_email(self, driver, wait, invalid_email):
        password = "Test123!"
        auth_page = AuthPage(driver, wait)

        auth_page.open_page("https://qa-desk.stand.praktikum-services.ru/")
        auth_page.open_login_registration_modal()
        auth_page.switch_to_registration()
        auth_page.fill_email(invalid_email)
        auth_page.fill_password(password)
        auth_page.confirm_password(password)
        auth_page.submit_registration()

        # ПРОВЕРКИ
        assert (
            auth_page.is_email_field_in_error_state()
        ), "Поле Email не выделено красным"
        actual_error_text = auth_page.get_email_error_message()
        expected_error_text = "Ошибка"
        assert (
            expected_error_text in actual_error_text
        ), f"Ожидалось сообщение '{expected_error_text}', но найдено: '{actual_error_text}'"

    # Тест 3: Регистрация существующего пользователя
    def test_registration_with_existing_email(self, driver, wait, create_test_user):
        self.wait = wait  # Сохраняем wait для использования в методах
        existing_email = create_test_user

        # 1. Нажимаем кнопку «Вход и регистрация»
        self._click_element("login_reg_button")

        # 2. Нажимаем кнопку «Нет аккаунта»
        self._click_element("no_account_button")

        # 3. Заполняем все поля формы регистрации
        self._fill_field("email_field", existing_email)
        self._fill_field("password_field", "NewPassword123!")
        self._fill_field("confirm_password_field", "NewPassword123!")

        # Нажимаем кнопку «Создать аккаунт»
        self._click_element("create_account_button")

        # 4. ПРОВЕРКИ согласно ТЗ
        # Проверка 1: поле Email выделено красным
        self._assert_element_displayed(
            "email_error_container_flexible",
            "Поле Email не выделено красным при ошибке",
        )

        # Проверка 2: поле «Пароль» выделено красным
        self._assert_element_displayed(
            "password_error_container_flexible",
            "Поле «Пароль» не выделено красным при ошибке",
        )

        # Проверка 3: поле «Повторите пароль» выделено красным
        self._assert_element_displayed(
            "confirm_password_error_container_flexible",
            "Поле «Повторите пароль» не выделено красным при ошибке",
        )

        # Проверка 4: под полем Email отображается сообщение «Ошибка»
        self._assert_text_in_element(
            "email_error_message_flexible",
            "Ошибка",
            "Ожидалось сообщение 'Ошибка', но найдено: '{actual_text}'",
        )
