from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_back_keyboard():
    """
    Создает клавиатуру с кнопкой "Назад в меню".
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Назад в меню")]
        ],
        resize_keyboard=True
    )
    return keyboard