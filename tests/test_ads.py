from constants import BASE_URL
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

        driver.get(BASE_URL)

        # Нажимаем кнопку «Разместить объявление»
        click_post_ad_button(driver)

        # Ожидаем появления модального окна авторизации и проверяем заголовок
        modal_title = ElementHelper.wait_for_visibility(
            driver, RegistrationPageLocators.MODAL_POPUP_TITLE
        )
        actual_title_text = modal_title.text
        expected_title_text = UITexts.UNAUTHORIZED_POST_AD_WARNING
        assert (
            actual_title_text == expected_title_text
        ), f"Заголовок модального окна некорректен. Ожидалось: {expected_title_text}"

    def test_post_ad_authorized(self, registered_user):
        """Тест: Создание объявления авторизованным пользователем"""
        user_data, driver = registered_user
        ad_data = AD_TEST_DATA["valid_ad"]
        driver.get(BASE_URL)

        # Нажимаем кнопку «Разместить объявление»
        click_post_ad_button(driver)

        # Заполняем форму объявления
        fill_ad_form(driver, ad_data)

        # Выбираем категорию и город
        select_category_and_city(driver)

        # Отправляем форму объявления
        submit_ad_form(driver)

        # Переходим в профиль пользователя
        navigate_to_profile(driver)

        # Ищем элемент объявления по заголовку
        ad_element = find_ad_in_profile_by_title(driver, ad_data["title"])

        # Проверка: объявление отображается в профиле
        assert (
            ad_element.is_displayed()
        ), f"Объявление '{ad_data['title']}' не отображается в профиле"
