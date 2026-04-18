from selenium.webdriver.common.by import By

# Локаторы для страницы авторизации/регистрации
AUTH_LOCATORS = {
    "login_reg_button": (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]"),
    "user_avatar_button": (By.CSS_SELECTOR, "button.circleSmall"),
    "no_account_button": (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]"),
    "email_field": (By.CSS_SELECTOR, "input[name='email']"),
    "password_field": (By.CSS_SELECTOR, "input[name='password']"),
    "confirm_password_field": (By.CSS_SELECTOR, "input[name='submitPassword']"),
    "create_account_button": (
        By.XPATH,
        "//button[contains(text(), 'Создать аккаунт')]",
    ),
    "user_avatar": (By.CSS_SELECTOR, "svg.svgSmall"),
    "user_name": (
        By.XPATH,
        "//*[contains(@class, 'profileText') and string-length(text()) > 0]",
    ),
    "email_error_container": (By.CSS_SELECTOR, ".input_inputError__fLUP9"),
    "email_error_container_flexible": (
        By.XPATH,
        "//div[contains(@class, 'input_inputError') and .//input[@name='email']]",
    ),
    "email_error_message": (By.CSS_SELECTOR, ".input_span__yWPqB"),
    "email_error_message_flexible": (
        By.XPATH,
        "//span[contains(@class, 'input_span') and contains(text(), 'Ошибка')]",
    ),
    "password_error_container": (
        By.XPATH,
        "//div[@class='input_inputError__fLUP9' and .//input[@name='password']]",
    ),
    "password_error_container_flexible": (
        By.XPATH,
        "//div[contains(@class, 'input_inputError') and .//input[@name='password']]",
    ),
    "confirm_password_error_container": (
        By.XPATH,
        "//div[@class='input_inputError__fLUP9' and .//input[@name='submitPassword']]",
    ),
    "confirm_password_error_container_flexible": (
        By.XPATH,
        "//div[contains(@class, 'input_inputError') and .//input[@name='submitPassword']]",
    ),
    "create_account_button_disabled": (
        By.XPATH,
        "//button[contains(text(), 'Создать аккаунт') and @disabled]",
    ),
    "loading_spinner": (
        By.CSS_SELECTOR,
        ".spinner, .loader, [class*='spinner'], [class*='loader']",
    ),
    "login_button": (By.XPATH, "//button[contains(text(), 'Войти')]"),
    "user_name_in_header": (By.CSS_SELECTOR, ".profileText.name"),
}

# Локаторы для главной страницы и создания объявлений
ADS_LOCATORS = {
    "post_ad_button": (By.XPATH, "//button[contains(text(), 'Разместить объявление')]"),
    "title_field": (By.CSS_SELECTOR, "input[name='name']"),
    "price_field": (By.CSS_SELECTOR, "input[name='price']"),
    "description_field": (By.CSS_SELECTOR, "textarea[name='description']"),
    "submit_ad_button": (By.XPATH, "//button[contains(text(), 'Опубликовать')]"),
    "my_ads_link": (
        By.CSS_SELECTOR,
        "a[href*='my-ads'], a[href*='/profile/ads'], a[class*='my-ads']",
    ),
    "modal_title": (By.CSS_SELECTOR, ".modal-title"),
    "ad_title_field": (By.CSS_SELECTOR, "input[name='title']"),
    "ad_description_field": (By.CSS_SELECTOR, "textarea[name='description']"),
    "ad_price_field": (By.CSS_SELECTOR, "input[name='price']"),
    "category_dropdown": (By.CSS_SELECTOR, "select[name='category']"),
    "city_dropdown": (By.CSS_SELECTOR, "select[name='city']"),
    "condition_new_radio": (By.XPATH, "//input[@value='new']/following-sibling::label"),
    "logout_button": (By.CSS_SELECTOR, "button.spanGlobal.btnSmall"),
    "ad_title_error": (
        By.XPATH,
        "//div[contains(@class, 'input_error') and .//input[@name='title']]/following::span",
    ),
    "ad_description_error": (
        By.XPATH,
        "//div[contains(@class, 'input_error') and .//textarea[@name='description']]/following::span",
    ),
    "ad_price_error": (
        By.XPATH,
        "//div[contains(@class, 'input_error') and .//input[@name='price']]/following::span",
    ),
    "publish_button_disabled": (
        By.XPATH,
        "//button[contains(text(), 'Опубликовать') and @disabled]",
    ),
    "success_message": (
        By.XPATH,
        "//div[contains(@class, 'success') or contains(text(), 'Успешно')]",
    ),
    "separator_between_user_and_post_ad": (By.CSS_SELECTOR, "div.line_line__CsoFB"),
    "profile_page_title": (By.XPATH, "//h1[contains(text(), 'Мой профиль')]"),
    "my_ads_page_title": (By.XPATH, "//h1[contains(text(), 'Мои объявления')]"),
    "created_ad_in_list": (
        By.XPATH,
        "//div[contains(@class, 'ad-item') or contains(@class, 'listing')]//div[contains(., '{title}')]",
    ),
    "ad_card": (By.CSS_SELECTOR, "div.card"),
    "ad_title_in_card": (By.CSS_SELECTOR, "div.card h2.h2"),
    "ad_price_in_card": (By.CSS_SELECTOR, "div.card div.price h2.h2"),
    "ad_location_in_card": (By.CSS_SELECTOR, "div.card h3.h3"),
    "edit_button_in_card": (By.CSS_SELECTOR, "div.card button.editButton"),
    "ad_card_by_title": (
        By.XPATH,
        "//div[@class='card' and .//h2[@class='h2' and contains(text(), '{title}')]",
    ),
    "ads_list_container": (
        By.CSS_SELECTOR,
        "div[class*='ads-list'], div[class*='listings']",
    ),
    "ad_in_profile_by_title": (
        By.XPATH,
        "//div[contains(@class, 'card')]//h2[contains(@class, 'h2') and contains(text(), '{}')]",
    ),
    "modal_auth_title": (
        By.XPATH,
        "//h1[contains(@class, 'h1') and contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]",
    ),
}
