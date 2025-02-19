import sqlite3

def init_db():
    """
    Инициализирует базу данных и создает таблицы, если они не существуют.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()

    # Таблица для пациентов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            phone_number TEXT
        )
    ''')

    # Таблица для услуг
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Таблица для посещений
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            service_id INTEGER NOT NULL,
            visit_date TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patients (id),
            FOREIGN KEY (service_id) REFERENCES services (id)
        )
    ''')

    conn.commit()
    conn.close()

# Инициализация базы данных при импорте
init_db()