from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
from constants import BASE_URL, REGISTRATION_PAGE, WAIT_TIMEOUT
from locators import RegistrationPageLocators, AdCreationLocators
from data import ErrorMessages


class ElementHelper:
    @staticmethod
    def wait_and_click(driver, locator, message=None):
        """Ожидает кликабельный элемент и кликает по нему"""
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        element = wait.until(EC.element_to_be_clickable(locator), message=message)
        element.click()
        return element

    @staticmethod
    def wait_and_input(driver, locator, text, message=None):
        """Ожидает поле ввода, очищает его и вводит текст"""
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        field = wait.until(EC.presence_of_element_located(locator), message=message)
        field.clear()
        field.send_keys(text)
        return field

    @staticmethod
    def wait_for_visibility(driver, locator, message=None):
        """Ожидает видимости элемента"""
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        return wait.until(EC.visibility_of_element_located(locator), message=message)

    @staticmethod
    def verify_element_not_present(driver, locator):
        """Проверяет, что элемент отсутствует в DOM"""
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(
            EC.invisibility_of_element_located(locator), "Элемент должен быть невидимым"
        )


def click_post_ad_button(driver):
    """Нажимает кнопку «Разместить объявление»"""
    ElementHelper.wait_and_click(
        driver,
        RegistrationPageLocators.POST_AD_BUTTON,
        ErrorMessages.BUTTON_POST_AD_NOT_FOUND,
    )


def register_user(driver, user_data):
    """Регистрирует пользователя с указанными данными"""
    driver.get(BASE_URL)

    ElementHelper.wait_and_click(
        driver,
        RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON,
        ErrorMessages.ELEMENT_AVATAR_AFTER_REGISTRATION_MISSING,
    )

    ElementHelper.wait_and_click(
        driver,
        RegistrationPageLocators.NO_ACCOUNT_BUTTON,
        ErrorMessages.BUTTON_NO_ACCOUNT_NOT_FOUND,
    )

    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(lambda d: REGISTRATION_PAGE in d.current_url)

    ElementHelper.wait_and_input(
        driver,
        RegistrationPageLocators.EMAIL_FIELD,
        user_data["email"],
        ErrorMessages.FIELD_EMAIL_NOT_FOUND,
    )

    ElementHelper.wait_and_input(
        driver,
        RegistrationPageLocators.PASSWORD_FIELD,
        user_data["password"],
        ErrorMessages.FIELD_PASSWORD_NOT_FOUND,
    )

    ElementHelper.wait_and_input(
        driver,
        RegistrationPageLocators.CONFIRM_PASSWORD_FIELD,
        user_data["password"],
        ErrorMessages.FIELD_CONFIRM_PASSWORD_NOT_FOUND,
    )

    ElementHelper.wait_and_click(
        driver,
        RegistrationPageLocators.CREATE_ACCOUNT_BUTTON,
        ErrorMessages.BUTTON_CREATE_ACCOUNT_NOT_FOUND,
    )

    ElementHelper.wait_for_visibility(
        driver,
        RegistrationPageLocators.USER_AVATAR_ELEMENT,
        ErrorMessages.ELEMENT_AVATAR_AFTER_REGISTRATION_MISSING,
    )


def logout_user(driver):
    """Выходит из аккаунта пользователя"""
    # Нажимаем кнопку «Выйти»
    ElementHelper.wait_and_click(
        driver,
        RegistrationPageLocators.LOGOUT_BUTTON,
        ErrorMessages.BUTTON_LOGOUT_NOT_FOUND,
    )

    # Ждём, пока аватар исчезнет
    ElementHelper.verify_element_not_present(
        driver, RegistrationPageLocators.USER_AVATAR_ELEMENT
    )


def get_unauthorized_warning_text(driver):
    """Возвращает текст модального окна для неавторизованного пользователя"""
    modal_title = ElementHelper.wait_for_visibility(
        driver,
        RegistrationPageLocators.MODAL_POPUP_TITLE,
        ErrorMessages.ELEMENT_MODAL_POPUP_NOT_DISPLAYED,
    )
    return modal_title.text.strip()


def navigate_to_profile(driver):
    """Переходит в профиль пользователя через клик по аватару"""
    ElementHelper.wait_and_click(
        driver,
        RegistrationPageLocators.USER_AVATAR_ELEMENT,
        "Кнопка аватара пользователя не найдена",
    )
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(EC.url_contains("/profile"))


def login_user(driver, user_data):
    """Выполняет вход пользователя"""

    ElementHelper.wait_and_click(
        driver,
        RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON,
        ErrorMessages.BUTTON_LOGIN_REGISTRATION_NOT_FOUND,
    )

    ElementHelper.wait_and_input(
        driver,
        RegistrationPageLocators.EMAIL_FIELD,
        user_data["email"],
        ErrorMessages.FIELD_EMAIL_NOT_FOUND,
    )

    ElementHelper.wait_and_input(
        driver,
        RegistrationPageLocators.PASSWORD_FIELD,
        user_data["password"],
        ErrorMessages.FIELD_PASSWORD_NOT_FOUND,
    )

    ElementHelper.wait_and_click(
        driver,
        RegistrationPageLocators.LOGIN_SUBMIT_BUTTON,
        ErrorMessages.BUTTON_LOGIN_SUBMIT_NOT_FOUND,
    )

    ElementHelper.verify_element_not_present(
        driver, RegistrationPageLocators.MODAL_WINDOW
    )


def fill_ad_form(driver, ad_data):
    """Заполняет форму создания объявления"""
    ElementHelper.wait_and_input(
        driver,
        AdCreationLocators.TITLE_FIELD,
        ad_data["title"],
        ErrorMessages.FIELD_TITLE_NOT_FOUND,
    )

    ElementHelper.wait_and_input(
        driver,
        AdCreationLocators.DESCRIPTION_FIELD,
        ad_data["description"],
        ErrorMessages.FIELD_DESCRIPTION_NOT_FOUND,
    )

    ElementHelper.wait_and_input(
        driver,
        AdCreationLocators.PRICE_FIELD,
        ad_data["price"],
        ErrorMessages.FIELD_PRICE_NOT_FOUND,
    )


def select_category_and_city(driver):
    """Выбирает категорию и город в форме объявления"""
    # Выбор категории
    ElementHelper.wait_and_click(
        driver,
        AdCreationLocators.CATEGORY_DROPDOWN_BUTTON,
        ErrorMessages.BUTTON_CATEGORY_DROPDOWN_NOT_FOUND,
    )
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(
        EC.presence_of_element_located(AdCreationLocators.DROP_DOWN_MENU_OPTIONS)
    )

    ElementHelper.wait_and_click(
        driver,
        AdCreationLocators.CATEGORY_TECHNOLOGY_OPTION,
        ErrorMessages.ELEMENT_CATEGORY_TECHNOLOGY_OPTION_MISSING,
    )

    # Выбор города
    ElementHelper.wait_and_click(
        driver,
        AdCreationLocators.CITY_DROPDOWN_BUTTON,
        ErrorMessages.BUTTON_CITY_DROPDOWN_NOT_FOUND,
    )
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(
        EC.presence_of_element_located(AdCreationLocators.DROP_DOWN_MENU_OPTIONS)
    )
    city_options = driver.find_elements(*AdCreationLocators.CITY_OPTIONS_IN_DROPDOWN)
    random.choice(city_options).click()


def submit_ad_form(driver):
    """Отправляет форму объявления"""
    ElementHelper.wait_and_click(
        driver,
        AdCreationLocators.SUBMIT_AD_BUTTON,
        ErrorMessages.BUTTON_SUBMIT_AD_NOT_FOUND,
    )
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(EC.url_changes(driver.current_url))


def find_ad_in_profile_by_title(driver, ad_title):
    """Ищет элемент объявления в профиле пользователя по его заголовку"""
    ad_locator = (
        AdCreationLocators.AD_IN_PROFILE_BY_TITLE[0],
        AdCreationLocators.AD_IN_PROFILE_BY_TITLE[1].format(ad_title),
    )
    return ElementHelper.wait_for_visibility(
        driver,
        ad_locator,
        f"Объявление с названием '{ad_title}' не найдено в блоке 'Мои объявления'",
    )


def get_auth_status(driver):
    """Возвращает статус авторизации пользователя (видимость ключевых элементов)"""
    avatar = ElementHelper.wait_for_visibility(
        driver,
        RegistrationPageLocators.USER_AVATAR_ELEMENT,
        ErrorMessages.ELEMENT_USER_AVATAR_NOT_VISIBLE,
    )

    user_name = ElementHelper.wait_for_visibility(
        driver,
        RegistrationPageLocators.USER_NAME_ELEMENT,
        ErrorMessages.ELEMENT_USER_NAME_NOT_VISIBLE_AFTER_LOGIN,
    )

    return {
        "avatar_visible": avatar.is_displayed(),
        "user_name": user_name.text.strip(),
    }


def is_login_button_visible(driver):
    """Возвращает состояние кнопки «Вход и регистрация» (видима/невидима)"""
    login_btn = ElementHelper.wait_for_visibility(
        driver,
        RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON,
        ErrorMessages.ELEMENT_LOGIN_REGISTRATION_BUTTON_AFTER_LOGOUT_MISSING,
    )
    return login_btn.is_displayed()
