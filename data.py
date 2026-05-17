class ErrorMessages:
    # Ошибки полей ввода
    FIELD_EMAIL_NOT_FOUND = "Не найдено поле email"
    FIELD_PASSWORD_NOT_FOUND = "Не найдено поле пароля"
    FIELD_CONFIRM_PASSWORD_NOT_FOUND = "Не найдено поле подтверждения пароля"
    FIELD_TITLE_NOT_FOUND = "Не найдено поле заголовка объявления"
    FIELD_DESCRIPTION_NOT_FOUND = "Не найдено поле описания"
    FIELD_PRICE_NOT_FOUND = "Не найдено поле цены"

    # Ошибки кнопок
    BUTTON_LOGIN_REGISTRATION_NOT_FOUND = "Не найдена кнопка 'Вход и регистрация'"
    BUTTON_LOGOUT_NOT_FOUND = "Не найдена кнопка выхода"
    BUTTON_POST_AD_NOT_FOUND = "Не найдена кнопка 'Разместить объявление'"
    BUTTON_CREATE_ACCOUNT_NOT_FOUND = "Не найдена кнопка создания аккаунта"
    BUTTON_NO_ACCOUNT_NOT_FOUND = "Не найдена кнопка 'Нет аккаунта'"
    BUTTON_LOGIN_SUBMIT_NOT_FOUND = "Не найдена кнопка отправки формы входа"
    BUTTON_CATEGORY_DROPDOWN_NOT_FOUND = (
        "Не найдена кнопка выпадающего списка категорий"
    )
    BUTTON_CITY_DROPDOWN_NOT_FOUND = "Не найдена кнопка выпадающего списка городов"
    BUTTON_SUBMIT_AD_NOT_FOUND = "Не найдена кнопка отправки формы объявления"

    # Ошибки элементов интерфейса
    ELEMENT_USER_AVATAR_NOT_VISIBLE = "Аватар не отображается"
    ELEMENT_AVATAR_AFTER_REGISTRATION_MISSING = "Аватар не появился после регистрации"
    ELEMENT_MODAL_POPUP_NOT_DISPLAYED = "Модальное окно с предупреждением не появилось"
    ELEMENT_CATEGORY_TECHNOLOGY_OPTION_MISSING = (
        "Не найдена опция категории 'Технологии'"
    )
    ELEMENT_USER_NAME_NOT_VISIBLE_AFTER_LOGIN = (
        "Имя пользователя не отображается после авторизации"
    )
    ELEMENT_LOGIN_REGISTRATION_BUTTON_AFTER_LOGOUT_MISSING = (
        "Кнопка 'Вход и регистрация' не отображается после выхода"
    )
    EXPECTED_ERROR_MESSAGE = "Ошибка"
    USER_NAME_DOES_NOT_MATCH = "Имя пользователя не соответствует ожидаемому"
    FIELD_EMAIL_HAS_NO_ERROR_CLASS = "Поле Email не выделено красным"
    FIELD_PASSWORD_HAS_NO_ERROR_CLASS = "Поле Пароль не выделено красным"
    FIELD_CONFIRM_PASSWORD_HAS_NO_ERROR_CLASS = (
        "Поле Повторите пароль не выделено красным"
    )

    # Специальные сообщения
    SPECIAL_USER_NAME_EMPTY = "Имя пользователя пустое"

    TEXT_EXPECTED_NOT_FOUND_IN_ACTUAL = "Ошибка: ожидаемый текст '{expected_text}' не найден в фактическом тексте '{actual_text}'"


class UITexts:
    UNAUTHORIZED_POST_AD_WARNING = "Чтобы разместить объявление, авторизуйтесь"
    EXPECTED_USER_NAME = "User."
    LOGIN_REGISTRATION_BUTTON_TEXT = "Вход и регистрация"


AD_TEST_DATA = {
    "valid_ad": {
        "title": "Тестовый товар",
        "description": "Описание тестового товара",
        "price": "1000",
    }
}
