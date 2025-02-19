from aiogram.types import Message
from database.visits import get_patient_visits
from database.patients import find_patient
from keyboards.main import get_main_keyboard
from keyboards.back import get_back_keyboard

def register_patient_visits_handlers(dp, current_state):
    @dp.message(lambda message: message.text == "Посещения пациента")
    async def cmd_patient_visits(message: Message):
        global current_state
        current_state = "PATIENT_VISITS"
        await message.answer(
            "Введите ФИО пациента для получения отчета:",
            reply_markup=get_back_keyboard()
        )

    @dp.message(lambda message: current_state == "PATIENT_VISITS")
    async def process_patient_visits(message: Message):
        global current_state
        patient = find_patient(message.text)
        if not patient:
            await message.answer("❌ Пациент не найден.", reply_markup=get_back_keyboard())
            return
        visits = get_patient_visits(patient[0])
        if visits:
            response = f"📊 Посещения пациента {patient[1]}:\n"
            for visit in visits:
                response += f"📅 {visit[0]} - {visit[1]} ({visit[2]} руб.)\n"
            await message.answer(response, reply_markup=get_main_keyboard())
        else:
            await message.answer("❌ Посещений не найдено.", reply_markup=get_back_keyboard())
        current_state = None