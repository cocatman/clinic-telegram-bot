from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_reports_keyboard():
    """
    Создает клавиатуру для работы с отчетами.
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Отчет за день")],
            [KeyboardButton(text="Отчет за месяц")],
            [KeyboardButton(text="Назад в меню")]
        ],
        resize_keyboard=True
    )
    return keyboard