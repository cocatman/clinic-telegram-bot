from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def create_keyboard(buttons: list, resize_keyboard: bool = True):
    """
    Создает клавиатуру на основе списка кнопок.
    :param buttons: Список кнопок (каждая кнопка — это список строк).
    :param resize_keyboard: Если True, кнопки подстраиваются под размер экрана.
    :return: Объект ReplyKeyboardMarkup.
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=button) for button in buttons],
        resize_keyboard=resize_keyboard
    )
    return keyboard