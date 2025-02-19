from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database.visits import add_visit
from database.patients import find_patient
from database.services import get_all_services
from validators import validate_datetime
from keyboards.main import get_main_keyboard
from keyboards.back import get_back_keyboard
from states import AddVisitState
from datetime import datetime, timedelta

router = Router()

@router.message(F.text == "Записать на прием")
async def cmd_add_visit(message: Message, state: FSMContext):
    """
    Обработчик для команды "Записать на прием".
    """
    await message.answer(
        "Введите ФИО пациента, которого хотите записать на прием:\n\n"
        "Пример: Иванов Иван Иванович",
        reply_markup=get_back_keyboard()
    )
    await state.set_state(AddVisitState.waiting_for_patient)

@router.message(AddVisitState.waiting_for_patient)
async def process_visit_patient(message: Message, state: FSMContext):
    """
    Обработчик для ввода ФИО пациента.
    """
    patient = find_patient(message.text)
    if not patient:
        await message.answer("❌ Пациент не найден. Попробуйте снова.", reply_markup=get_back_keyboard())
        return
    await state.update_data(patient=patient)  # Сохраняем данные пациента
    await message.answer(
        "Теперь введите название услуги:\n\n"
        "Пример: Консультация",
        reply_markup=get_back_keyboard()
    )
    await state.set_state(AddVisitState.waiting_for_service)

@router.message(AddVisitState.waiting_for_service)
async def process_visit_service(message: Message, state: FSMContext):
    """
    Обработчик для ввода услуги.
    """
    services = get_all_services()
    service = next((s for s in services if s[1] == message.text), None)
    if not service:
        await message.answer("❌ Услуга не найдена. Попробуйте снова.", reply_markup=get_back_keyboard())
        return
    await state.update_data(service=service)  # Сохраняем данные услуги
    await message.answer(
        "Теперь введите дату и время приема в формате ГГГГ-ММ-ДДTЧЧ:ММ:\n\n"
        "Пример: 2025-02-10T14:00",
        reply_markup=get_back_keyboard()
    )
    await state.set_state(AddVisitState.waiting_for_date)

@router.message(AddVisitState.waiting_for_date)
async def process_visit_date(message: Message, state: FSMContext):
    """
    Обработчик для ввода даты и времени.
    """
    try:
        start_time = datetime.strptime(message.text, "%Y-%m-%dT%H:%M")
        end_time = start_time + timedelta(hours=1)
        start_time_str = start_time.isoformat()
        end_time_str = end_time.isoformat()

        data = await state.get_data()  # Получаем сохраненные данные
        patient = data.get("patient")
        service = data.get("service")

        add_visit(patient[0], service[0], message.text)

        await message.answer(
            f"✅ Посещение для {patient[1]} успешно добавлено!",
            reply_markup=get_main_keyboard()
        )
    except ValueError:
        await message.answer("❌ Неверный формат даты и времени. Используйте формат ГГГГ-ММ-ДДTЧЧ:ММ.", reply_markup=get_back_keyboard())
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}", reply_markup=get_back_keyboard())
    finally:
        await state.clear()

def register_add_visit_handlers(dp):
    """
    Регистрирует обработчики для записи на прием.
    """
    dp.include_router(router)