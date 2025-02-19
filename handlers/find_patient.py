from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from database.patients import find_patient
from keyboards.back import get_back_keyboard

def register_find_patient_handlers(dp, current_state, temp_data):
    @dp.message(lambda message: message.text == "Найти пациента")
    async def cmd_find_patient(message: Message):
        global current_state
        current_state = "FIND_PATIENT"
        await message.answer(
            "Введите фамилию пациента для поиска:",
            reply_markup=get_back_keyboard()
        )

    @dp.message(lambda message: current_state == "FIND_PATIENT")
    async def process_find_patient(message: Message):
        global current_state, temp_data
        surname = message.text.strip()
        patient = find_patient(surname)
        if patient:
            temp_data['patient_id'] = patient[0]
            temp_data['patient_name'] = patient[1]

            custom_keyboard = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="Редактировать пациента")],
                    [KeyboardButton(text="Назад в меню")]
                ],
                resize_keyboard=True
            )

            await message.answer(
                f"✅ Найден пациент: {patient[1]}, Телефон: {patient[2]}\n\n"
                "Выберите действие:",
                reply_markup=custom_keyboard
            )
        else:
            await message.answer("❌ Пациент не найден.", reply_markup=get_back_keyboard())
        current_state = None