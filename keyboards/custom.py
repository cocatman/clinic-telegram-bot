from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_edit_patient_keyboard():
    """
    Создает клавиатуру для редактирования пациента.
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Редактировать пациента")],
            [KeyboardButton(text="Назад в меню")]
        ],
        resize_keyboard=True
    )
    return keyboard