from aiogram.types import Message
from database.services import add_service
from keyboards.main import get_main_keyboard
from keyboards.back import get_back_keyboard

def register_add_service_handlers(dp, current_state):
    @dp.message(lambda message: message.text == "Добавить услугу")
    async def cmd_add_service(message: Message):
        global current_state
        current_state = "ADD_SERVICE"
        await message.answer(
            "Введите данные услуги:\n"
            "Название услуги и цену через запятую.\n\n"
            "Пример: Консультация, 1500",
            reply_markup=get_back_keyboard()
        )

    @dp.message(lambda message: current_state == "ADD_SERVICE")
    async def process_service_data(message: Message):
        global current_state
        try:
            name, price = map(str.strip, message.text.split(','))
            add_service(name, float(price))
            await message.answer(f"✅ Услуга {name} успешно добавлена!", reply_markup=get_main_keyboard())
        except Exception as e:
            await message.answer("❌ Ошибка в формате данных. Попробуйте снова.", reply_markup=get_back_keyboard())
        finally:
            current_state = None