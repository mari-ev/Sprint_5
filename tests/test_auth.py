import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import AUTH_LOCATORS, ADS_LOCATORS


class TestAuth:
    def _click_element(self, locator_key):
        """Клик по элементу с ожиданием кликабельности."""
        element = self.wait.until(
            EC.element_to_be_clickable(
                AUTH_LOCATORS.get(locator_key, ADS_LOCATORS.get(locator_key))
            )
        )
        element.click()

    def _fill_field(self, locator_key, text):
        """Заполнение поля с ожиданием возможности ввода."""
        field = self.wait.until(
            EC.element_to_be_clickable(
                AUTH_LOCATORS.get(locator_key, ADS_LOCATORS.get(locator_key))
            )
        )
        field.clear()
        field.send_keys(text)

    def _assert_element_displayed(self, locator_dict, locator_key, error_message):
        """Проверка видимости элемента."""
        element = self.wait.until(
            EC.presence_of_element_located(locator_dict[locator_key])
        )
        assert element.is_displayed(), error_message

    def _assert_element_invisible(self, locator_dict, locator_key, error_message):
        """Проверка невидимости элемента."""
        self.wait.until(EC.invisibility_of_element_located(locator_dict[locator_key]))

    def _get_element_location(self, locator_dict, locator_key):
        """Получение координат элемента."""
        element = self.wait.until(
            EC.presence_of_element_located(locator_dict[locator_key])
        )
        return element.location

    # Тест 1: Первый логин пользователя
    def test_user_first_login(self, driver, wait, create_test_user):
        self.wait = wait
        email, password = create_test_user

        # 1. Открываем главную страницу
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        # 2. Нажимаем кнопку «Вход и регистрация»
        self._click_element("login_reg_button")

        # 3. Заполняем поле email
        self._fill_field("email_field", email)

        # 4. Заполняем поле пароля
        self._fill_field("password_field", password)

        # 5. Нажимаем кнопку «Войти»
        self._click_element("login_button")

        # Ждём полной загрузки главной страницы после авторизации
        self.wait.until(EC.url_contains("qa-desk.stand.praktikum-services.ru"))

        # ПРОВЕРКИ согласно ТЗ

        # Проверка 1: произошёл переход на главную после авторизации
        post_ad_btn = self.wait.until(
            EC.presence_of_element_located(ADS_LOCATORS["post_ad_button"])
        )
        assert (
            post_ad_btn.is_displayed()
        ), "Не произошёл переход на главную после авторизации"

        # Проверка 2: отображается аватар пользователя
        user_avatar = self.wait.until(
            EC.visibility_of_element_located(AUTH_LOCATORS["user_avatar_button"])
        )
        assert (
            user_avatar.is_displayed()
        ), "Аватар пользователя не отображается после авторизации"

        # Проверка 3: отображается имя пользователя User
        user_name = self.wait.until(
            EC.presence_of_element_located(AUTH_LOCATORS["user_name_in_header"])
        )
        actual_name = user_name.text.strip().rstrip(".")
        assert (
            actual_name != ""
        ), f"Имя пользователя не отображается, найдено: '{actual_name}'"
        assert (
            "User" in actual_name
        ), f"Ожидалось имя 'User', но найдено: '{actual_name}'"

        # Проверка 4: отображается разделитель между User и кнопкой «Разместить объявление»
        separator = self.wait.until(
            EC.presence_of_element_located(
                ADS_LOCATORS["separator_between_user_and_post_ad"]
            )
        )
        assert (
            separator.is_displayed()
        ), "Разделитель между User и кнопкой не отображается"

        # Проверки расположения элементов
        avatar_location = self._get_element_location(
            AUTH_LOCATORS, "user_avatar_button"
        )
        name_location = self._get_element_location(AUTH_LOCATORS, "user_name_in_header")
        separator_location = self._get_element_location(
            ADS_LOCATORS, "separator_between_user_and_post_ad"
        )
        post_ad_location = self._get_element_location(ADS_LOCATORS, "post_ad_button")

        # Проверка 5: все элементы находятся в верхней части экрана (y < 200)
        assert avatar_location["y"] < 200, "Аватар не находится в верхней части экрана"
        assert (
            name_location["y"] < 200
        ), "Имя пользователя не находится в верхней части экрана"
        assert (
            separator_location["y"] < 200
        ), "Разделитель не находится в верхней части экрана"
        assert (
            post_ad_location["y"] < 200
        ), "Кнопка 'Разместить объявление' не находится в верхней части экрана"

        # Проверка 6: элементы расположены строго слева направо в правильном порядке
        elements = [
            (avatar_location["x"], "аватар"),
            (name_location["x"], "имя User"),
            (separator_location["x"], "разделитель"),
            (post_ad_location["x"], "кнопка 'Разместить объявление'"),
        ]
        sorted_elements = sorted(elements, key=lambda x: x[0])
        expected_order = [
            "аватар",
            "имя User",
            "разделитель",
            "кнопка 'Разместить объявление'",
        ]
        actual_order = [element[1] for element in sorted_elements]
        assert actual_order == expected_order, (
            f"Неправильный порядок элементов. Ожидалось: {expected_order}, "
            f"фактически: {actual_order}"
        )

        # Проверка 7: все элементы находятся примерно на одной высоте (±30 px)
        y_coords = [
            avatar_location["y"],
            name_location["y"],
            separator_location["y"],
            post_ad_location["y"],
        ]
        min_y, max_y = min(y_coords), max(y_coords)
        assert (max_y - min_y) < 30, "Элементы расположены на разной высоте"

    # Тест 2: Разлогин пользователя
    def test_user_logout(self, driver, wait, create_test_user):
        self.wait = wait
        email, password = create_test_user

        # 1. Открываем главную страницу
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        # 2. Нажимаем кнопку «Вход и регистрация»
        self._click_element("login_reg_button")

        # 3. Заполняем поле email
        self._fill_field("email_field", email)

        # 4. Заполняем поле пароля
        self._fill_field("password_field", password)

        # 5. Нажимаем кнопку «Войти»
        self._click_element("login_button")

        # 6. Ждём полной загрузки интерфейса после авторизации
        self.wait.until(
            EC.visibility_of_element_located(AUTH_LOCATORS["user_avatar_button"])
        )
        self.wait.until(
            EC.visibility_of_element_located(AUTH_LOCATORS["user_name_in_header"])
        )

        # 7. Выполняем разлогин
        self._click_element("logout_button")

        # 8. Проверяем скрытие элементов авторизованного пользователя
        self._assert_element_invisible(
            AUTH_LOCATORS,
            "user_avatar_button",
            "Аватар пользователя не скрылся после разлогина",
        )
        self._assert_element_invisible(
            AUTH_LOCATORS,
            "user_name_in_header",
            "Имя пользователя не скрылось после разлогина",
        )

        # 9. Проверяем появление кнопки авторизации
        login_reg_btn_final = self.wait.until(
            EC.element_to_be_clickable(AUTH_LOCATORS["login_reg_button"])
        )
        assert (
            login_reg_btn_final.is_displayed()
        ), "Кнопка 'Вход и регистрация' не отображается после разлогина"
