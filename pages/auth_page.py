from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import AUTH_LOCATORS, ADS_LOCATORS


class AuthPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_page(self, url):
        """Открывает страницу по URL"""
        self.driver.get(url)

    def open_login_registration_modal(self):
        """Нажимает кнопку «Вход и регистрация»"""
        btn = self.wait.until(
            EC.element_to_be_clickable(AUTH_LOCATORS["login_reg_button"])
        )
        btn.click()

    def switch_to_registration(self):
        """Нажимает кнопку «Нет аккаунта»"""
        btn = self.wait.until(
            EC.element_to_be_clickable(AUTH_LOCATORS["no_account_button"])
        )
        btn.click()

    def fill_email(self, email):
        """Заполняет поле Email"""
        field = self.wait.until(
            EC.element_to_be_clickable(AUTH_LOCATORS["email_field"])
        )
        field.send_keys(email)

    def fill_password(self, password):
        """Заполняет поле Пароль"""
        field = self.wait.until(
            EC.element_to_be_clickable(AUTH_LOCATORS["password_field"])
        )
        field.send_keys(password)

    def confirm_password(self, password):
        """Заполняет поле «Повторите пароль»"""
        field = self.wait.until(
            EC.visibility_of_element_located(AUTH_LOCATORS["confirm_password_field"])
        )
        field.send_keys(password)

    def submit_registration(self):
        """Нажимает кнопку «Создать аккаунт»"""
        btn = self.wait.until(
            EC.element_to_be_clickable(AUTH_LOCATORS["create_account_button"])
        )
        btn.click()

    def wait_for_modal_close(self):
        """Ждём закрытия модального окна регистрации"""
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//h2[contains(text(), 'Зарегистрироваться')]")
            )
        )

    def is_post_ad_button_displayed(self):
        """Проверяет, отображается ли кнопка «Разместить объявление»"""
        try:
            btn = self.wait.until(
                EC.visibility_of_element_located(ADS_LOCATORS["post_ad_button"])
            )
            return btn.is_displayed()
        except:
            return False

    def is_user_avatar_displayed(self):
        """Проверяет, отображается ли аватар пользователя"""
        try:
            avatar = self.wait.until(
                EC.visibility_of_element_located(AUTH_LOCATORS["user_avatar"])
            )
            return avatar.is_displayed()
        except:
            return False

    def get_user_name(self):
        """Получает текст имени пользователя"""
        name_element = self.wait.until(
            EC.visibility_of_element_located(AUTH_LOCATORS["user_name"])
        )
        return name_element.text.strip()

    def is_email_field_in_error_state(self):
        """Проверяет, что поле Email обведено красным (в состоянии ошибки)"""
        try:
            container = self.wait.until(
                EC.presence_of_element_located(AUTH_LOCATORS["email_error_container"])
            )
            return container.is_displayed()
        except:
            return False

    def get_email_error_message(self):
        """Получает текст сообщения об ошибке под полем Email"""
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(AUTH_LOCATORS["email_error_message"])
            )
            return error_element.text.strip()
        except:
            return ""

    def is_password_field_in_error_state(self):
        """Проверяет, что поле «Пароль» обведено красным (в состоянии ошибки)"""
        try:
            container = self.wait.until(
                EC.presence_of_element_located(
                    AUTH_LOCATORS["password_error_container_flexible"]
                )
            )
            return container.is_displayed()
        except:
            return False

    def is_confirm_password_field_in_error_state(self):
        """Проверяет, что поле «Повторите пароль» обведено красным (в состоянии ошибки)"""
        try:
            container = self.wait.until(
                EC.presence_of_element_located(
                    AUTH_LOCATORS["confirm_password_error_container_flexible"]
                )
            )
            return container.is_displayed()
        except:
            return False

    def get_email_error_message_flexible(self):
        """Получает текст сообщения об ошибке под полем Email (гибкий локатор)"""
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(
                    AUTH_LOCATORS["email_error_message_flexible"]
                )
            )
            return error_element.text.strip()
        except:
            return ""
