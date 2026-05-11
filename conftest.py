import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from constants import BASE_URL, WAIT_TIMEOUT
from locators import RegistrationPageLocators


@pytest.fixture
def get_driver():
    """Фикстура для создания и закрытия драйвера Chrome для каждого теста"""
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@pytest.fixture
def generate_test_data():
    """Фикстура для генерации тестовых данных"""
    fake = Faker()
    return {
        "email": fake.email(),
        "password": fake.password(
            length=8, special_chars=True, digits=True, upper_case=True, lower_case=True
        ),
    }


@pytest.fixture
def generate_invalid_email_test_data():
    """Фикстура для генерации данных с некорректным email"""
    fake = Faker()
    return {
        "invalid_email": "not-an-email",
        "valid_password": fake.password(
            length=8, special_chars=True, digits=True, upper_case=True, lower_case=True
        ),
    }


@pytest.fixture(scope="session")
def registered_and_logged_out_user():
    """
    1. Регистрирует пользователя.
    2. Выходит из аккаунта (нажимая кнопку «Выйти» рядом с аватаром).
    3. Возвращает данные пользователя для повторного использования.
    Выполняется один раз за сессию.
    """
    # Создаём драйвер для регистрации и выхода
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    # Генерируем данные
    fake = Faker()
    test_data = {
        "email": fake.email(),
        "password": fake.password(
            length=8, special_chars=True, digits=True, upper_case=True, lower_case=True
        ),
    }

    try:
        # Шаг 1: Регистрация пользователя
        driver.get(BASE_URL)

        # Нажимаем «Вход и регистрация»
        login_reg_btn = wait.until(
            EC.element_to_be_clickable(
                RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON
            )
        )
        login_reg_btn.click()

        # Нажимаем «Нет аккаунта»
        no_account_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        )
        no_account_btn.click()
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.EMAIL_FIELD))

        # Заполняем email
        email_field = wait.until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(test_data["email"])

        # Заполняем пароль
        password_field = wait.until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_FIELD)
        )
        password_field.clear()
        password_field.send_keys(test_data["password"])

        # Подтверждаем пароль
        confirm_password_field = wait.until(
            EC.presence_of_element_located(
                RegistrationPageLocators.CONFIRM_PASSWORD_FIELD
            )
        )
        confirm_password_field.clear()
        confirm_password_field.send_keys(test_data["password"])

        # Создаём аккаунт
        create_account_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        )
        create_account_btn.click()

        # Ждём появления аватара (успешная регистрация)
        wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.USER_AVATAR_ELEMENT
            )
        )

        # Шаг 2: Выход из аккаунта — нажимаем кнопку «Выйти» (находится рядом с аватаром)
        logout_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGOUT_BUTTON)
        )
        logout_btn.click()

        # Ждём, пока аватар исчезнет (пользователь вышел)
        wait.until(
            EC.invisibility_of_element_located(
                RegistrationPageLocators.USER_AVATAR_ELEMENT
            )
        )

        return test_data  # возвращаем данные для использования в других тестах

    finally:
        driver.quit()  # закрываем драйвер после регистрации и выхода
