import sqlite3

def add_patient(full_name: str, phone_number: str):
    """
    Добавляет нового пациента в базу данных.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patients (full_name, phone_number)
        VALUES (?, ?)
    ''', (full_name, phone_number))
    conn.commit()
    conn.close()

def find_patient(surname: str):
    """
    Ищет пациента по фамилии (частичное совпадение).
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM patients WHERE full_name LIKE ?
    ''', (f"%{surname}%",))
    patient = cursor.fetchone()
    conn.close()
    return patient

def edit_patient(patient_id: int, full_name: str, phone_number: str):
    """
    Редактирует данные пациента в базе данных.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE patients
        SET full_name = ?, phone_number = ?
        WHERE id = ?
    ''', (full_name, phone_number, patient_id))
    conn.commit()
    conn.close()

def get_all_patients():
    """
    Возвращает список всех пациентов.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    conn.close()
    return patients