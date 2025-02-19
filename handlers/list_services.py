from aiogram.types import Message
from database.services import get_all_services
from keyboards.main import get_main_keyboard

def register_list_services_handlers(dp):
    """
    Регистрирует обработчики для показа списка услуг.
    """
    @dp.message(lambda message: message.text == "Список услуг")
    async def cmd_list_services(message: Message):
        """
        Обработчик для команды "Список услуг".
        """
        services = get_all_services()
        if services:
            response = "📋 Список услуг:\n"
            for service in services:
                response += f"🔹 {service[1]} - {service[2]} руб.\n"
            await message.answer(response, reply_markup=get_main_keyboard())
        else:
            await message.answer("❌ Услуги пока не добавлены.", reply_markup=get_main_keyboard())