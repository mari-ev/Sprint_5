import pytest
from selenium.webdriver.support.ui import WebDriverWait
from constants import BASE_URL, WAIT_TIMEOUT
from data import UITexts, AD_TEST_DATA
from helpers import (
    click_post_ad_button,
    fill_ad_form,
    select_category_and_city,
    submit_ad_form,
    navigate_to_profile,
    find_ad_in_profile_by_title,
    ElementHelper,
)
from locators import RegistrationPageLocators


class TestPostAd:
    """Тесты для проверки создания объявлений"""

    def test_post_ad_unauthorized(self, get_driver):
        """Тест: Попытка создания объявления неавторизованным пользователем"""
        driver = get_driver
        wait = WebDriverWait(driver, WAIT_TIMEOUT)

        driver.get(BASE_URL)

        # Нажимаем кнопку «Разместить объявление»
        click_post_ad_button(driver, wait)

        # Ожидаем появления модального окна авторизации и проверяем заголовок
        modal_title = ElementHelper.wait_for_visibility(
            driver, wait, RegistrationPageLocators.MODAL_POPUP_TITLE
        )
        actual_title_text = modal_title.text
        expected_title_text = UITexts.UNAUTHORIZED_POST_AD_WARNING
        assert (
            actual_title_text == expected_title_text
        ), f"Заголовок модального окна некорректен. Ожидалось: {expected_title_text}"

    def test_post_ad_authorized(self, registered_user):
        """Тест: Создание объявления авторизованным пользователем"""
        user_data, driver, wait = registered_user
        ad_data = AD_TEST_DATA["valid_ad"]
        driver.get(BASE_URL)

        # Нажимаем кнопку «Разместить объявление»
        click_post_ad_button(driver, wait)

        # Заполняем форму объявления
        fill_ad_form(driver, wait, ad_data)

        # Выбираем категорию и город
        select_category_and_city(driver, wait)

        # Отправляем форму объявления
        submit_ad_form(driver, wait)

        # Переходим в профиль пользователя
        navigate_to_profile(driver, wait)

        # Ищем элемент объявления по заголовку
        ad_element = find_ad_in_profile_by_title(driver, wait, ad_data["title"])

        # Проверка: объявление отображается в профиле
        assert (
            ad_element.is_displayed()
        ), f"Объявление '{ad_data['title']}' не отображается в профиле"
