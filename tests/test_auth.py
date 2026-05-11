import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import BASE_URL, WAIT_TIMEOUT
from locators import RegistrationPageLocators


class TestUserLoginLogout:
    """Тесты для проверки авторизации и выхода пользователя"""

    def test_user_login(self, get_driver, registered_and_logged_out_user):
        driver = get_driver
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        test_data = registered_and_logged_out_user

        driver.get(BASE_URL)

        login_reg_btn = wait.until(
            EC.element_to_be_clickable(
                RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON
            )
        )
        login_reg_btn.click()

        email_field = wait.until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(test_data["email"])

        password_field = driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(test_data["password"])

        login_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_SUBMIT_BUTTON)
        )
        login_btn.click()

        wait.until(
            EC.invisibility_of_element_located(RegistrationPageLocators.MODAL_WINDOW)
        )

        avatar = wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.USER_AVATAR_ELEMENT
            )
        )
        assert (
            avatar.is_displayed()
        ), "Аватар пользователя не отображается после авторизации"

        user_name = wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.USER_NAME_ELEMENT)
        )
        assert (
            user_name.is_displayed()
        ), "Имя пользователя не отображается после авторизации"
        assert (
            "User" in user_name.text
        ), f"Ожидалось имя 'User', но найдено: {user_name.text}"

    def test_user_logout(self, get_driver, registered_and_logged_out_user):
        driver = get_driver
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        test_data = registered_and_logged_out_user

        driver.get(BASE_URL)

        login_reg_btn = wait.until(
            EC.element_to_be_clickable(
                RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON
            )
        )
        login_reg_btn.click()

        email_field = wait.until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(test_data["email"])

        password_field = driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(test_data["password"])

        login_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_SUBMIT_BUTTON)
        )
        login_btn.click()

        wait.until(
            EC.invisibility_of_element_located(RegistrationPageLocators.MODAL_WINDOW)
        )

        logout_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGOUT_BUTTON)
        )
        logout_btn.click()

        login_reg_btn = wait.until(
            EC.element_to_be_clickable(
                RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON
            )
        )
        assert (
            login_reg_btn.is_displayed()
        ), "Кнопка 'Вход и регистрация' отображается после выхода"

        avatar_invisible = wait.until(
            EC.invisibility_of_element_located(
                RegistrationPageLocators.USER_AVATAR_ELEMENT
            ),
            message="Аватар должен быть невидимым после выхода",
        )
        assert avatar_invisible, "Аватар пользователя всё не отображается после выхода"

        name_invisible = wait.until(
            EC.invisibility_of_element_located(
                RegistrationPageLocators.USER_NAME_ELEMENT
            ),
            message="Имя пользователя должно быть невидимым после выхода",
        )
        assert name_invisible, "Имя пользователя всё ещё отображается после выхода"
