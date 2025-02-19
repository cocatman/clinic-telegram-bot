from aiogram.types import Message
from database.patients import edit_patient
from validators import validate_phone_number
from keyboards.main import get_main_keyboard
from keyboards.back import get_back_keyboard

def register_edit_patient_handlers(dp, current_state, temp_data):
    @dp.message(lambda message: message.text == "Редактировать пациента")
    async def cmd_edit_patient(message: Message):
        global current_state
        current_state = "EDIT_PATIENT_DATA"
        await message.answer(
            "Введите новые данные пациента (ФИО и номер телефона через запятую):\n\n"
            "Пример: Иванов Иван Иванович, +79161234567",
            reply_markup=get_back_keyboard()
        )

    @dp.message(lambda message: current_state == "EDIT_PATIENT_DATA")
    async def process_edit_patient_data(message: Message):
        global current_state, temp_data
        try:
            full_name, phone_number = map(str.strip, message.text.split(','))
            if not validate_phone_number(phone_number):
                await message.answer("❌ Неверный формат номера телефона. Попробуйте снова.", reply_markup=get_back_keyboard())
                return

            patient_id = temp_data.get('patient_id')
            if not patient_id:
                await message.answer("❌ Ошибка: ID пациента не найден.", reply_markup=get_back_keyboard())
                return

            edit_patient(patient_id, full_name, phone_number)
            await message.answer(f"✅ Данные пациента {full_name} успешно обновлены!", reply_markup=get_main_keyboard())
        except Exception as e:
            await message.answer(f"❌ Ошибка: {e}", reply_markup=get_back_keyboard())
        finally:
            current_state = None
            temp_data = {}