from faker import Faker

fake = Faker()


def _generate_password():
    """Генерация пароля с фиксированными параметрами"""
    return fake.password(
        length=8, special_chars=True, digits=True, upper_case=True, lower_case=True
    )


def generate_test_data():
    """Генерирует данные для успешной регистрации: email, пароль, подтверждение пароля (одинаковые)"""
    password = _generate_password()
    return {
        "email": fake.email(),
        "password": password,
        "confirm_password": password,  # одинаковый пароль для подтверждения
    }


def generate_invalid_email_test_data():
    """Генерирует данные с некорректным email"""
    valid_password = _generate_password()
    return {
        "email": "not-an-email",  # ← ключ теперь "email" (как ожидает хелпер)
        "password": valid_password,  # ← ключ "password" (как ожидает хелпер)
        "confirm_password": valid_password,
    }
