from aiogram.types import Message, FSInputFile
from database.visits import get_visits_by_day, get_visits_by_month
from reports import create_excel_report
from keyboards.main import get_main_keyboard
from keyboards.back import get_back_keyboard

def register_reports_handlers(dp, current_state):
    @dp.message(lambda message: message.text == "Отчет за день")
    async def cmd_report_day(message: Message):
        global current_state
        current_state = "REPORT_DAY"
        await message.answer(
            "Введите дату в формате ГГГГ-ММ-ДД:\n\n"
            "Пример: 2025-02-10",
            reply_markup=get_back_keyboard()
        )

    @dp.message(lambda message: message.text == "Отчет за месяц")
    async def cmd_report_month(message: Message):
        global current_state
        current_state = "REPORT_MONTH"
        await message.answer(
            "Введите год и месяц в формате ГГГГ-ММ:\n\n"
            "Пример: 2025-02",
            reply_markup=get_back_keyboard()
        )

    @dp.message(lambda message: current_state in ["REPORT_DAY", "REPORT_MONTH"])
    async def process_report_data(message: Message):
        global current_state
        try:
            if current_state == "REPORT_DAY":
                data = get_visits_by_day(message.text)
                filename = f"report_day_{message.text}.xlsx"
            elif current_state == "REPORT_MONTH":
                year, month = message.text.split('-')
                data = get_visits_by_month(year, month)
                filename = f"report_month_{message.text}.xlsx"

            if not data:
                await message.answer("❌ Данные за указанный период не найдены.", reply_markup=get_main_keyboard())
                return

            create_excel_report(data, filename)
            file = FSInputFile(filename)
            await message.answer_document(
                document=file,
                caption=f"📊 Отчет за {message.text}",
                reply_markup=get_main_keyboard()
            )
        except Exception as e:
            await message.answer(f"❌ Ошибка: {e}", reply_markup=get_main_keyboard())
        finally:
            current_state = None