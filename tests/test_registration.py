import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from constants import BASE_URL, WAIT_TIMEOUT


class TestUserRegistration:

    def test_user_registration(self, get_driver, generate_test_data):
        """Тест регистрации нового пользователя"""
        driver = get_driver
        test_data = generate_test_data
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, WAIT_TIMEOUT)

        login_reg_btn = wait.until(
            EC.element_to_be_clickable(
                RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON
            )
        )
        login_reg_btn.click()

        no_account_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        )
        no_account_btn.click()
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.EMAIL_FIELD))

        email_field = wait.until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(test_data["email"])

        password_field = wait.until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_FIELD)
        )
        password_field.clear()
        password_field.send_keys(test_data["password"])

        confirm_password_field = wait.until(
            EC.presence_of_element_located(
                RegistrationPageLocators.CONFIRM_PASSWORD_FIELD
            )
        )
        confirm_password_field.clear()
        confirm_password_field.send_keys(test_data["password"])

        create_account_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        )
        create_account_btn.click()

        avatar = wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.USER_AVATAR_ELEMENT
            )
        )
        assert (
            avatar.is_displayed()
        ), "Аватар пользователя не отображается после регистрации"

        username_element = wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.USER_NAME_ELEMENT)
        )
        assert (
            username_element.text.strip() == "User."
        ), "Имя пользователя не соответствует ожидаемому"

    def test_registration_with_invalid_email(
        self, get_driver, generate_invalid_email_test_data
    ):
        """Тест регистрации с некорректным email"""
        driver = get_driver
        test_data = generate_invalid_email_test_data
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        driver.get(BASE_URL)

        login_reg_btn = wait.until(
            EC.element_to_be_clickable(
                RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON
            )
        )
        login_reg_btn.click()

        no_account_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        )
        no_account_btn.click()
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.EMAIL_FIELD))

        email_field = wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(test_data["invalid_email"])

        password_field = wait.until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_FIELD)
        )
        password_field.clear()
        password_field.send_keys(test_data["valid_password"])

        confirm_password_field = wait.until(
            EC.presence_of_element_located(
                RegistrationPageLocators.CONFIRM_PASSWORD_FIELD
            )
        )
        confirm_password_field.clear()
        confirm_password_field.send_keys(test_data["valid_password"])

        create_account_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        )
        create_account_btn.click()

        email_error_field = wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR_FIELD)
        )

        error_message = wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.ERROR_MESSAGE_UNDER_EMAIL
            )
        )
        assert (
            error_message.text == "Ошибка"
        ), "Сообщение об ошибке не отображается или текст не соответствует"

    def test_registration_existing_user(
        self, get_driver, registered_and_logged_out_user
    ):
        """Тест регистрации уже существующего пользователя"""
        driver = get_driver
        test_data = registered_and_logged_out_user
        wait = WebDriverWait(driver, WAIT_TIMEOUT)

        driver.get(BASE_URL)

        login_reg_btn = wait.until(
            EC.element_to_be_clickable(
                RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON
            )
        )
        login_reg_btn.click()

        no_account_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        )
        no_account_btn.click()

        wait.until(EC.presence_of_element_located(RegistrationPageLocators.EMAIL_FIELD))

        email_field = wait.until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(test_data["email"])

        password_field = wait.until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_FIELD)
        )
        password_field.clear()
        password_field.send_keys(test_data["password"])

        confirm_password_field = wait.until(
            EC.presence_of_element_located(
                RegistrationPageLocators.CONFIRM_PASSWORD_FIELD
            )
        )
        confirm_password_field.clear()
        confirm_password_field.send_keys(test_data["password"])

        create_account_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        )
        create_account_btn.click()

        email_error_field = wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR_FIELD)
        )
        password_error_field = wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.PASSWORD_ERROR_FIELD
            )
        )
        confirm_password_error_field = wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.CONFIRM_PASSWORD_ERROR_FIELD
            )
        )

        error_message = wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.ERROR_MESSAGE_UNDER_EMAIL
            )
        )
        assert (
            error_message.text == "Ошибка"
        ), "Сообщение об ошибке не отображается или текст не соответствует"
