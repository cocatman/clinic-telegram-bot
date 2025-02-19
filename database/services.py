import sqlite3

def add_service(name: str, price: float):
    """
    Добавляет новую услугу в базу данных.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO services (name, price)
        VALUES (?, ?)
    ''', (name, price))
    conn.commit()
    conn.close()

def get_all_services():
    """
    Возвращает список всех услуг.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM services')
    services = cursor.fetchall()
    conn.close()
    return services

def find_service(name: str):
    """
    Ищет услугу по названию.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM services WHERE name = ?
    ''', (name,))
    service = cursor.fetchone()
    conn.close()
    return service