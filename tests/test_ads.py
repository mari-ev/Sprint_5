import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from constants import BASE_URL, WAIT_TIMEOUT
from locators import RegistrationPageLocators, AdCreationLocators


class TestPostAd:
    """Тесты для проверки размещения объявления (авторизованный и неавторизованный пользователь)"""

    def test_post_ad_unauthorized(self, get_driver):
        """Тест: Создание объявления неавторизованным пользователем"""
        driver = get_driver
        wait = WebDriverWait(driver, WAIT_TIMEOUT)

        driver.get(BASE_URL)

        post_ad_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.POST_AD_BUTTON)
        )
        post_ad_btn.click()

        modal_title = wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.MODAL_POPUP_TITLE)
        )

        expected_text = "Чтобы разместить объявление, авторизуйтесь"
        actual_text = modal_title.text

        assert (
            expected_text in actual_text
        ), f"Ошибка: ожидаемый текст '{expected_text}' не найден в фактическом тексте '{actual_text}'"

        driver.quit()

    def test_post_ad_authorized(self, get_driver, registered_and_logged_out_user):
        """Тест: Создание объявления авторизованным пользователем"""
        driver = get_driver
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        test_data = registered_and_logged_out_user
        ad_title = "Тестовый товар"
        ad_price = "1000"

        driver.get(BASE_URL)

        login_reg_btn = wait.until(
            EC.element_to_be_clickable(
                RegistrationPageLocators.LOGIN_REGISTRATION_BUTTON
            )
        )
        login_reg_btn.click()

        email_field = wait.until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(test_data["email"])

        password_field = driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(test_data["password"])

        login_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_SUBMIT_BUTTON)
        )
        login_btn.click()

        wait.until(
            EC.invisibility_of_element_located(RegistrationPageLocators.MODAL_WINDOW)
        )

        post_ad_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.POST_AD_BUTTON)
        )
        post_ad_btn.click()

        title_field = wait.until(
            EC.presence_of_element_located(AdCreationLocators.TITLE_FIELD)
        )
        title_field.send_keys(ad_title)

        description_field = wait.until(
            EC.presence_of_element_located(AdCreationLocators.DESCRIPTION_FIELD)
        )
        description_field.send_keys("Описание тестового товара")

        price_field = wait.until(
            EC.presence_of_element_located(AdCreationLocators.PRICE_FIELD)
        )
        price_field.send_keys(ad_price)

        category_dropdown_btn = wait.until(
            EC.element_to_be_clickable(AdCreationLocators.CATEGORY_DROPDOWN_BUTTON)
        )
        category_dropdown_btn.click()

        wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "dropDownMenu_optionsMobile__LmXZM")
            )
        )

        category_option = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@class='dropDownMenu_optionsMobile__LmXZM']//button//span[contains(text(), 'Технологии')]",
                )
            )
        )
        category_option.click()

        condition_option = wait.until(
            EC.element_to_be_clickable(AdCreationLocators.CONDITION_USED_LABEL)
        )
        condition_option.click()

        city_dropdown_btn = wait.until(
            EC.element_to_be_clickable(AdCreationLocators.CITY_DROPDOWN_BUTTON)
        )
        city_dropdown_btn.click()

        wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "dropDownMenu_optionsMobile__LmXZM")
            )
        )

        city_options = driver.find_elements(
            By.XPATH, "//div[@class='dropDownMenu_optionsMobile__LmXZM']//button//span"
        )
        random.choice(city_options).click()

        submit_btn = wait.until(
            EC.element_to_be_clickable(AdCreationLocators.SUBMIT_AD_BUTTON)
        )
        submit_btn.click()

        wait.until(EC.url_changes(driver.current_url))

        avatar_btn = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.USER_AVATAR_ELEMENT)
        )
        avatar_btn.click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        created_ad_locator = (
            AdCreationLocators.AD_IN_PROFILE_BY_TITLE[0],
            AdCreationLocators.AD_IN_PROFILE_BY_TITLE[1].format(ad_title),
        )
        created_ad = wait.until(EC.visibility_of_element_located(created_ad_locator))

        assert (
            created_ad.is_displayed()
        ), f"Созданное объявление с названием '{ad_title}' отображается в профиле пользователя"
