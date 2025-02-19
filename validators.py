import re
from datetime import datetime

def validate_phone_number(phone_number: str) -> bool:
    """
    Проверяет, соответствует ли номер телефона формату.
    Допустимые форматы:
    - +79161234567
    - 89161234567
    - 79161234567
    """
    pattern = r"^\+?\d{10,15}$"  # Пример: +79161234567 или 89161234567
    return re.match(pattern, phone_number) is not None

def validate_date(date_str: str) -> bool:
    """
    Проверяет, соответствует ли строка формату даты ГГГГ-ММ-ДД.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_datetime(datetime_str: str) -> bool:
    """
    Проверяет, соответствует ли строка формату даты и времени ГГГГ-ММ-ДДTЧЧ:ММ.
    """
    try:
        datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M")
        return True
    except ValueError:
        return False