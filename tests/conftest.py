import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AUTH_LOCATORS

fake = Faker()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 30)


@pytest.fixture
def test_credentials():
    """Фикстура для генерации уникальных email и пароля для каждого теста"""
    email = fake.email()
    password = fake.password(
        length=8, special_chars=True, digits=True, upper_case=True, lower_case=True
    )
    return email, password


@pytest.fixture
def create_test_user(driver, wait):
    """
    Фикстура: создаёт тестового пользователя, выходит из аккаунта и возвращает email и пароль.
    Пароль генерируется через Faker.
    """
    email = fake.email()
    password = fake.password(
        length=8, special_chars=True, digits=True, upper_case=True, lower_case=True
    )

    # 1. Открываем страницу
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    # 2. Открываем модальное окно авторизации
    login_reg_btn = wait.until(
        EC.element_to_be_clickable(AUTH_LOCATORS["login_reg_button"])
    )
    login_reg_btn.click()

    # 3. Нажимаем «Нет аккаунта»
    no_account_btn = wait.until(
        EC.element_to_be_clickable(AUTH_LOCATORS["no_account_button"])
    )
    no_account_btn.click()

    # 4. Заполняем форму регистрации
    email_field = wait.until(EC.element_to_be_clickable(AUTH_LOCATORS["email_field"]))
    email_field.send_keys(email)

    password_field = wait.until(
        EC.element_to_be_clickable(AUTH_LOCATORS["password_field"])
    )
    password_field.send_keys(password)

    confirm_password_field = wait.until(
        EC.visibility_of_element_located(AUTH_LOCATORS["confirm_password_field"])
    )
    confirm_password_field.send_keys(password)

    # 5. Нажимаем «Создать аккаунт»
    create_account_btn = wait.until(
        EC.element_to_be_clickable(AUTH_LOCATORS["create_account_button"])
    )
    create_account_btn.click()

    # 6. Ждём появления кнопки «Выйти» (по тексту внутри <button>)
    logout_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Выйти']"))
    )

    # 7. Нажимаем кнопку «Выйти»
    logout_btn.click()

    # 8. Ждём появления кнопки «Вход и регистрация» после выхода
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
        )
    )

    yield email, password  # передаём email и пароль в тест
