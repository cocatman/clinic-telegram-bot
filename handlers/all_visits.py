from aiogram.types import Message
from database.visits import get_all_visits
from keyboards.main import get_main_keyboard

def register_all_visits_handlers(dp):
    @dp.message(lambda message: message.text == "Все посещения")
    async def cmd_all_visits(message: Message):
        visits = get_all_visits()
        if visits:
            response = "📊 Отчет по всем посещениям:\n"
            for visit in visits:
                response += f"👤 {visit[0]} - 📅 {visit[3]} - 💼 {visit[1]} ({visit[2]} руб.)\n"
            await message.answer(response, reply_markup=get_main_keyboard())
        else:
            await message.answer("❌ Посещений не найдено.", reply_markup=get_main_keyboard())