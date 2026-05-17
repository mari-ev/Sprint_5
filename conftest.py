import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from data_generation import (
    generate_test_data,
    generate_invalid_email_test_data,
)
from helpers import (
    register_user,
    logout_user,
    login_user,
)
from constants import WAIT_TIMEOUT


@pytest.fixture(scope="function")
def wait(get_driver):
    """Фикстура для ожидания с таймаутом из constants.WAIT_TIMEOUT"""
    return WebDriverWait(get_driver, WAIT_TIMEOUT)


@pytest.fixture(scope="function")
def get_driver():
    """Фикстура для создания и закрытия драйвера Chrome для каждого теста"""
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@pytest.fixture
def test_data():
    return generate_test_data()  # Используем напрямую импортированную функцию


@pytest.fixture
def invalid_email_test_data():
    return generate_invalid_email_test_data()  # Из правильного модуля


@pytest.fixture(scope="function")
def registered_user(get_driver):
    """
    Фикстура: регистрирует пользователя и возвращает его данные.
    Выполняется для каждого теста (scope="function").
    """
    driver = get_driver
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    user_data = generate_test_data()  # Теперь функция доступна
    register_user(driver, wait, user_data)
    yield user_data, driver, wait


@pytest.fixture(scope="function")
def logged_out_user(registered_user):
    """
    Фикстура: берёт зарегистрированного пользователя и выходит из его аккаунта.
    Использует тот же драйвер, что и registered_user.
    """
    user_data, driver, wait = registered_user

    try:
        logout_user(driver, wait)
    except Exception as e:
        print(f"Ошибка при выходе из аккаунта: {e}")  # Логируем ошибку
    yield user_data
