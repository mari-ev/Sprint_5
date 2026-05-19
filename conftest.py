import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from data_generation import generate_test_data
from helpers import register_user, logout_user


@pytest.fixture(scope="function")
def get_driver():
    """Фикстура для создания и закрытия драйвера Chrome для каждого теста"""
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def registered_user(get_driver):
    """
    Фикстура: регистрирует пользователя и возвращает его данные.
    Выполняется для каждого теста (scope="function").
    """
    driver = get_driver
    user_data = generate_test_data()
    register_user(driver, user_data)
    return user_data, driver


@pytest.fixture(scope="function")
def logged_out_user(registered_user):
    """
    Фикстура: берёт зарегистрированного пользователя и выходит из его аккаунта.
    Использует тот же драйвер, что и registered_user.
    """
    user_data, driver = registered_user

    try:
        logout_user(driver)
    except Exception as e:
        print(f"Ошибка при выходе из аккаунта: {e}")
    yield user_data
