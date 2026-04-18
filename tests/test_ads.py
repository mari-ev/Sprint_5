import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from locators import ADS_LOCATORS, AUTH_LOCATORS


class TestPostAd:
    def _click_element(self, locator_dict, locator_key):
        """Клик по элементу с ожиданием кликабельности."""
        element = self.wait.until(EC.element_to_be_clickable(locator_dict[locator_key]))
        element.click()

    def _fill_field(self, locator_dict, locator_key, text):
        """Заполнение поля с ожиданием возможности ввода."""
        field = self.wait.until(EC.element_to_be_clickable(locator_dict[locator_key]))
        field.clear()
        field.send_keys(text)

    def _assert_element_displayed(self, locator_dict, locator_key, error_message):
        """Проверка видимости элемента."""
        element = self.wait.until(
            EC.presence_of_element_located(locator_dict[locator_key])
        )
        assert element.is_displayed(), error_message

    def _scroll_and_click(self, element):
        """Прокрутка к элементу и клик через ActionChains."""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    # Тест 1: Создание объявления неавторизованным пользователем
    def test_post_ad_unauthorized(self, driver, wait):
        self.driver = driver
        self.wait = wait

        # Открываем главную страницу
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        # Нажимаем кнопку «Разместить объявление»
        self._click_element(ADS_LOCATORS, "post_ad_button")

        # Проверка 1: появление модального окна авторизации
        modal_title = self.wait.until(
            EC.visibility_of_element_located(ADS_LOCATORS["modal_auth_title"])
        )
        assert (
            modal_title.text.strip() == "Чтобы разместить объявление, авторизуйтесь"
        ), "Заголовок модального окна некорректный"

        # Проверка 2: отображение кнопки «Вход и регистрация» в модальном окне
        self._assert_element_displayed(
            AUTH_LOCATORS,
            "login_reg_button",
            "Кнопка 'Вход и регистрация' не отображается в модальном окне",
        )

    # Тест 2: Создание объявления авторизованным пользователем
    def test_create_ad_authorized(self, driver, wait, create_test_user):
        self.driver = driver
        self.wait = wait
        email, password = create_test_user
        expected_title = "Тестовый товар для проверки"
        expected_price = "2500"
        expected_description = "Полное описание тестового товара для проверки функционала создания объявлений"

        # ШАГ 1: Авторизация
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        self._click_element(AUTH_LOCATORS, "login_reg_button")
        self._fill_field(AUTH_LOCATORS, "email_field", email)
        self._fill_field(AUTH_LOCATORS, "password_field", password)
        self._click_element(AUTH_LOCATORS, "login_button")

        # Проверка авторизации
        user_avatar = self.wait.until(
            EC.visibility_of_element_located(AUTH_LOCATORS["user_avatar_button"])
        )
        assert (
            user_avatar.is_displayed()
        ), "Авторизация не прошла — аватар пользователя не отображается"

        # ШАГ 2: Открытие формы создания объявления
        self._click_element(ADS_LOCATORS, "post_ad_button")

        # ШАГ 3: Заполнение формы объявления
        self._fill_field(ADS_LOCATORS, "title_field", expected_title)
        self._fill_field(ADS_LOCATORS, "price_field", expected_price)
        self._fill_field(ADS_LOCATORS, "description_field", expected_description)

        # ШАГ 4: Публикация объявления
        self._click_element(ADS_LOCATORS, "submit_ad_button")
        self.wait.until(EC.url_contains("qa-desk.stand.praktikum-services.ru"))

        # Ждём полной загрузки страницы после публикации объявления
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )

        # ШАГ 5: Переход в профиль пользователя через аватар
        user_avatar_btn = self.wait.until(
            EC.element_to_be_clickable(AUTH_LOCATORS["user_avatar_button"])
        )
        self._scroll_and_click(user_avatar_btn)

        # Ожидаемый URL страницы профиля
        expected_profile_url = "https://qa-desk.stand.praktikum-services.ru/profile"
        self.wait.until(EC.url_to_be(expected_profile_url))

        # ШАГ 6: Проверка отображения страницы профиля
        profile_title = self.wait.until(
            EC.visibility_of_element_located(ADS_LOCATORS["profile_page_title"])
        )
        assert "Мой профиль" in profile_title.text, "Страница профиля не открылась"

        # ШАГ 7: Проверка раздела «Мои объявления»
        my_ads_title = self.wait.until(
            EC.visibility_of_element_located(ADS_LOCATORS["my_ads_page_title"])
        )
        assert my_ads_title.is_displayed(), "Раздел 'Мои объявления' не отображается"

        # ШАГ 8: Проверка наличия созданного объявления
        ad_locator_template = ADS_LOCATORS["ad_in_profile_by_title"]
        ad_locator = (
            ad_locator_template[0],
            ad_locator_template[1].format(expected_title),
        )

        found_ad = self.wait.until(EC.presence_of_element_located(ad_locator))
        assert (
            found_ad.is_displayed()
        ), f"Объявление '{expected_title}' не найдено в списке объявлений"
