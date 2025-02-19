from aiogram.fsm.state import State, StatesGroup

class AddPatientState(StatesGroup):
    waiting_for_data = State()  # Состояние ожидания ввода данных пациента

class AddVisitState(StatesGroup):
    waiting_for_patient = State()  # Состояние ожидания ввода ФИО пациента
    waiting_for_service = State()  # Состояние ожидания ввода услуги
    waiting_for_date = State()  # Состояние ожидания ввода даты