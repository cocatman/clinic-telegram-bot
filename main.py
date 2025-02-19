from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from config import API_TOKEN
from handlers import register_handlers
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота с использованием DefaultBotProperties
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # Устанавливаем HTML-форматирование по умолчанию
)

# Инициализация диспетчера с использованием MemoryStorage для FSM
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Регистрация всех обработчиков
register_handlers(dp)

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен!")
    dp.run_polling(bot)