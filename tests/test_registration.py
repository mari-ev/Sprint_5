from constants import BASE_URL
from locators import RegistrationPageLocators
from data_generation import generate_invalid_email_test_data, generate_test_data
from helpers import (
    register_user,
    get_auth_status,
    ElementHelper,
)
from data import ErrorMessages, UITexts


class TestUserRegistration:
    def test_user_registration(self, get_driver):
        """Тест регистрации нового пользователя"""
        driver = get_driver
        test_data = generate_test_data()
        register_user(driver, test_data)

        # Проверка перехода на главную (игнорируем хеш-фрагмент)
        assert driver.current_url.startswith(
            BASE_URL
        ), "Не произошёл переход на главную страницу после регистрации"

        # Проверяем статус авторизации через хелпер
        auth_status = get_auth_status(driver)
        assert auth_status[
            "avatar_visible"
        ], "Аватар пользователя не отображается после регистрации"
        assert (
            auth_status["user_name"] == UITexts.EXPECTED_USER_NAME
        ), f"Имя пользователя не соответствует ожидаемому. Ожидалось: {UITexts.EXPECTED_USER_NAME}"

    def test_registration_with_invalid_email(self, get_driver):
        """Тест регистрации с некорректным email"""
        driver = get_driver
        test_data = generate_invalid_email_test_data()

        driver.get(BASE_URL)

        # Используем хелперы для выполнения действий
        ElementHelper.wait_and_click(
            driver, RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON
        )
        ElementHelper.wait_and_click(driver, RegistrationPageLocators.NO_ACCOUNT_BUTTON)

        ElementHelper.wait_and_input(
            driver,
            RegistrationPageLocators.EMAIL_FIELD,
            test_data["email"],
        )
        ElementHelper.wait_and_input(
            driver,
            RegistrationPageLocators.PASSWORD_FIELD,
            test_data["password"],
        )
        ElementHelper.wait_and_input(
            driver,
            RegistrationPageLocators.CONFIRM_PASSWORD_FIELD,
            test_data["password"],
        )

        ElementHelper.wait_and_click(
            driver, RegistrationPageLocators.CREATE_ACCOUNT_BUTTON
        )

        # Проверка всех трёх контейнеров
        error_containers = [
            (RegistrationPageLocators.EMAIL_FIELD_ERROR_PARENT, "Email поле"),
            (RegistrationPageLocators.PASSWORD_FIELD_ERROR_PARENT, "Пароль поле"),
            (
                RegistrationPageLocators.CONFIRM_PASSWORD_FIELD_ERROR_PARENT,
                "Подтверждение пароля поле",
            ),
        ]

        for locator, field_name in error_containers:
            container = ElementHelper.wait_for_visibility(driver, locator)
            assert (
                container.is_displayed()
            ), f"{field_name} не обведено красным при ошибке валидации"

        # Проверка сообщения об ошибке
        error_message = ElementHelper.wait_for_visibility(
            driver, RegistrationPageLocators.ERROR_MESSAGE_UNDER_EMAIL
        )
        actual_error_text = error_message.text
        expected_error_text = ErrorMessages.EXPECTED_ERROR_MESSAGE
        assert (
            actual_error_text == expected_error_text
        ), f"Сообщение об ошибке не соответствует. Ожидалось: {expected_error_text}"

    def test_registration_existing_user(self, get_driver, logged_out_user):
        """Тест регистрации уже существующего пользователя"""
        driver = get_driver
        test_data = logged_out_user

        driver.get(BASE_URL)

        # Используем хелперы для выполнения действий
        ElementHelper.wait_and_click(
            driver, RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON
        )
        ElementHelper.wait_and_click(driver, RegistrationPageLocators.NO_ACCOUNT_BUTTON)

        ElementHelper.wait_and_input(
            driver, RegistrationPageLocators.EMAIL_FIELD, test_data["email"]
        )
        ElementHelper.wait_and_input(
            driver, RegistrationPageLocators.PASSWORD_FIELD, test_data["password"]
        )
        ElementHelper.wait_and_input(
            driver,
            RegistrationPageLocators.CONFIRM_PASSWORD_FIELD,
            test_data["password"],
        )

        ElementHelper.wait_and_click(
            driver, RegistrationPageLocators.CREATE_ACCOUNT_BUTTON
        )

        # Проверка всех трёх контейнеров
        error_containers = [
            (RegistrationPageLocators.EMAIL_FIELD_ERROR_PARENT, "Email поле"),
            (RegistrationPageLocators.PASSWORD_FIELD_ERROR_PARENT, "Пароль поле"),
            (
                RegistrationPageLocators.CONFIRM_PASSWORD_FIELD_ERROR_PARENT,
                "Подтверждение пароля поле",
            ),
        ]

        for locator, field_name in error_containers:
            container = ElementHelper.wait_for_visibility(driver, locator)
            assert (
                container.is_displayed()
            ), f"{field_name} не обведено красным при ошибке валидации"

        # Проверка сообщения об ошибке
        error_message = ElementHelper.wait_for_visibility(
            driver, RegistrationPageLocators.ERROR_MESSAGE_UNDER_EMAIL
        )
        actual_error_text = error_message.text
        expected_error_text = ErrorMessages.EXPECTED_ERROR_MESSAGE
        assert (
            actual_error_text == expected_error_text
        ), f"Сообщение об ошибке не соответствует. Ожидалось: {expected_error_text}"
