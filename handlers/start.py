from aiogram.filters import Command
from aiogram.types import Message
from keyboards.main import get_main_keyboard

def register_start_handlers(dp):
    @dp.message(Command("start"))
    async def cmd_start(message: Message):
        await message.answer(
            "👋 Привет! Я бот для учета пациентов в клинике.\n\n"
            "Вот что я могу:\n"
            "1. Добавить пациента\n"
            "2. Добавить услугу\n"
            "3. Записать пациента на прием\n"
            "4. Найти пациента\n"
            "5. Посмотреть посещения пациента\n"
            "6. Посмотреть все посещения\n"
            "7. Сформировать отчеты\n"
            "8. Показать список услуг\n\n"
            "Выберите действие:",
            reply_markup=get_main_keyboard()
        )