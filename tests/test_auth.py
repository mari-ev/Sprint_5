from constants import BASE_URL
from data import ErrorMessages, UITexts
from helpers import (
    login_user,
    logout_user,
    is_login_button_visible,
    get_auth_status,
    ElementHelper,
)
from locators import RegistrationPageLocators


class TestUserLoginLogout:
    """Тесты для проверки авторизации и выхода пользователя"""

    def test_user_login(self, get_driver, logged_out_user):
        """Тест авторизации пользователя: переход на главную, аватар и имя User отображаются"""
        driver = get_driver
        test_data = logged_out_user

        driver.get(BASE_URL)

        # Используем хелпер для авторизации
        login_user(driver, test_data)

        # Проверка перехода на главную
        assert driver.current_url.startswith(
            BASE_URL
        ), "Не произошёл переход на главную страницу после авторизации"

        # Проверяем статус авторизации через хелпер
        auth_status = get_auth_status(driver)
        assert auth_status[
            "avatar_visible"
        ], ErrorMessages.ELEMENT_USER_AVATAR_NOT_VISIBLE
        assert (
            auth_status["user_name"] == UITexts.EXPECTED_USER_NAME
        ), ErrorMessages.USER_NAME_DOES_NOT_MATCH

    def test_user_logout(self, get_driver, logged_out_user):
        """Тест выхода пользователя: аватар и имя исчезают, появляется кнопка 'Вход и регистрация'"""
        driver = get_driver
        test_data = logged_out_user

        driver.get(BASE_URL)

        # Авторизуемся через хелпер
        login_user(driver, test_data)

        # Выходим из аккаунта через хелпер
        logout_user(driver)

        # ПРОВЕРКИ ПОСЛЕ ВЫХОДА

        # 1. Проверяем, что аватар исчез (используем готовый хелпер)
        ElementHelper.verify_element_not_present(
            driver, RegistrationPageLocators.USER_AVATAR_ELEMENT
        )

        # 2. Проверяем, что имя пользователя исчезло
        ElementHelper.verify_element_not_present(
            driver, RegistrationPageLocators.USER_NAME_ELEMENT
        )

        # 3. Проверяем появление кнопки 'Вход и регистрация'
        login_btn_visible = is_login_button_visible(driver)
        assert (
            login_btn_visible
        ), f"Кнопка '{UITexts.LOGIN_REGISTRATION_BUTTON_TEXT}' не отображается после выхода"
