import sqlite3

def execute_query(query: str, params: tuple = ()):
    """
    Выполняет SQL-запрос и возвращает результат.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result