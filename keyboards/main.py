from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    """
    Создает главное меню с кнопками.
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Добавить пациента"), KeyboardButton(text="Добавить услугу")],
            [KeyboardButton(text="Записать на прием"), KeyboardButton(text="Найти пациента")],
            [KeyboardButton(text="Посещения пациента"), KeyboardButton(text="Все посещения")],
            [KeyboardButton(text="Отчет за день"), KeyboardButton(text="Отчет за месяц")],
            [KeyboardButton(text="Список услуг")]
        ],
        resize_keyboard=True  # Кнопки подстраиваются под размер экрана
    )
    return keyboard