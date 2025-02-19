from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database.patients import add_patient
from validators import validate_phone_number
from keyboards.main import get_main_keyboard
from keyboards.back import get_back_keyboard
from states import AddPatientState

router = Router()

@router.message(F.text == "Добавить пациента")
async def cmd_add_patient(message: Message, state: FSMContext):
    """
    Обработчик для команды "Добавить пациента".
    """
    await message.answer(
        "Введите данные пациента:\n"
        "ФИО и номер телефона через запятую.\n\n"
        "Пример: Иванов Иван Иванович, +79161234567",
        reply_markup=get_back_keyboard()
    )
    await state.set_state(AddPatientState.waiting_for_data)

@router.message(AddPatientState.waiting_for_data)
async def process_patient_data(message: Message, state: FSMContext):
    """
    Обработчик для ввода данных пациента.
    """
    try:
        full_name, phone_number = map(str.strip, message.text.split(','))
        if not validate_phone_number(phone_number):
            await message.answer("❌ Неверный формат номера телефона. Попробуйте снова.", reply_markup=get_back_keyboard())
            return
        add_patient(full_name, phone_number)
        await message.answer(f"✅ Пациент {full_name} успешно добавлен!", reply_markup=get_main_keyboard())
    except Exception as e:
        await message.answer("❌ Ошибка в формате данных. Попробуйте снова.", reply_markup=get_back_keyboard())
    finally:
        await state.clear()

def register_add_patient_handlers(dp):
    """
    Регистрирует обработчики для добавления пациента.
    """
    dp.include_router(router)