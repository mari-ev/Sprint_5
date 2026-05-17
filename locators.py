from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    """Локаторы элементов страницы регистрации"""

    LOGIN_REGISTRATION_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Вход и регистрация')]",
    )
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(., 'Нет аккаунта')]")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and contains(@class, 'buttonPrimary') and contains(., 'Создать аккаунт')]",
    )
    USER_AVATAR_ELEMENT = (By.CLASS_NAME, "circleSmall")
    USER_NAME_ELEMENT = (By.CSS_SELECTOR, "h3.profileText.name")
    MODAL_WINDOW = (By.CLASS_NAME, "homePage_modal__zSdUB")
    EMAIL_ERROR_FIELD = (
        By.XPATH,
        "//div[contains(@class, 'input_inputError__fLUP9')]//input[@name='email']",
    )
    ERROR_MESSAGE_UNDER_EMAIL = (
        By.XPATH,
        "//div[contains(@class, 'popUp_inputColumn__RgD8n')]//span[contains(@class, 'input_span__yWPqB') and text()='Ошибка']",
    )
    PASSWORD_ERROR_FIELD = (
        By.XPATH,
        "//div[contains(@class, 'input_inputError__fLUP9')]//input[@name='password']",
    )
    CONFIRM_PASSWORD_ERROR_FIELD = (
        By.XPATH,
        "//div[contains(@class, 'input_inputError__fLUP9')]//input[@name='submitPassword']",
    )
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'spanGlobal') and contains(@class, 'btnSmall') and @type='button' and normalize-space()='Выйти']",
    )

    LOGIN_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and contains(., 'Войти')]",
    )
    POST_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    MODAL_POPUP_TITLE = (
        By.XPATH,
        "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]",
    )

    EMAIL_FIELD_ERROR_PARENT = (
        By.XPATH,
        "//div[contains(@class, 'input_inputError__fLUP9') and .//input[@name='email']]",
    )
    PASSWORD_FIELD_ERROR_PARENT = (
        By.XPATH,
        "//div[contains(@class, 'input_inputError__fLUP9') and .//input[@name='password']]",
    )
    CONFIRM_PASSWORD_FIELD_ERROR_PARENT = (
        By.XPATH,
        "//div[contains(@class, 'input_inputError__fLUP9') and .//input[@name='submitPassword']]",
    )


class AdCreationLocators:

    TITLE_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_FIELD = (By.CSS_SELECTOR, "input[name='price']")
    CONDITION_USED_LABEL = (
        By.XPATH,
        "//div[@class='createListing_inputRadio__ApFGD']//label[@class='h2' and text()='Б/У']",
    )
    CONDITION_USED_ACTIVE_INDICATOR = (
        By.XPATH,
        "//div[@class='createListing_inputRadio__ApFGD']//label[@class='h2' and text()='Б/У']/preceding-sibling::div[contains(@class, 'inputActive')]",
    )
    CONDITION_NEW_LABEL = (
        By.XPATH,
        "//div[@class='createListing_inputRadio__ApFGD']//label[@class='h2' and text()='Новый']",
    )
    CONDITION_NEW_ACTIVE_INDICATOR = (
        By.XPATH,
        "//div[@class='createListing_inputRadio__ApFGD']//label[@class='h2' and text()='Новый']/preceding-sibling::div[contains(@class, 'inputActive')]",
    )
    SUBMIT_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    MY_ADS_PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]")
    AD_IN_PROFILE_BY_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'card')]//h2[contains(@class, 'h2') and contains(text(), '{}')]",
    )
    CATEGORY_DROPDOWN_BUTTON = (
        By.XPATH,
        "//input[@name='category']/following::button[contains(@class, 'dropDownMenu_arrowDown')][1]",
    )
    CITY_DROPDOWN_BUTTON = (
        By.XPATH,
        "//input[@name='city']/following::button[contains(@class, 'dropDownMenu_arrowDown')][1]",
    )
    CITY_OPTIONS_IN_DROPDOWN = (
        By.XPATH,
        "//div[@class='dropDownMenu_optionsMobile__LmXZM']//button//span",
    )
    DROP_DOWN_MENU_OPTIONS = (By.CLASS_NAME, "dropDownMenu_optionsMobile__LmXZM")
    CATEGORY_TECHNOLOGY_OPTION = (
        By.XPATH,
        "//div[@class='dropDownMenu_optionsMobile__LmXZM']//button//span[contains(text(), 'Технологии')]",
    )
    CATEGORY_OPTIONS = (By.CSS_SELECTOR, ".category-option, .dropdown-item")
    CITY_OPTIONS = (By.CSS_SELECTOR, ".city-option, .dropdown-item")
