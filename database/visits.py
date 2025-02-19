import sqlite3
from datetime import datetime

def add_visit(patient_id: int, service_id: int, visit_date: str):
    """
    Добавляет новое посещение в базу данных.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO visits (patient_id, service_id, visit_date)
        VALUES (?, ?, ?)
    ''', (patient_id, service_id, visit_date))
    conn.commit()
    conn.close()

def get_patient_visits(patient_id: int):
    """
    Возвращает список посещений для конкретного пациента.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT visits.visit_date, services.name, services.price
        FROM visits
        JOIN services ON visits.service_id = services.id
        WHERE visits.patient_id = ?
    ''', (patient_id,))
    visits = cursor.fetchall()
    conn.close()
    return visits

def get_all_visits():
    """
    Возвращает список всех посещений.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT patients.full_name, services.name, services.price, visits.visit_date
        FROM visits
        JOIN patients ON visits.patient_id = patients.id
        JOIN services ON visits.service_id = services.id
    ''')
    visits = cursor.fetchall()
    conn.close()
    return visits

def get_visits_by_day(date: str):
    """
    Возвращает список посещений за указанный день.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT patients.full_name, services.name, services.price, visits.visit_date
        FROM visits
        JOIN patients ON visits.patient_id = patients.id
        JOIN services ON visits.service_id = services.id
        WHERE DATE(visits.visit_date) = ?
    ''', (date,))
    visits = cursor.fetchall()
    conn.close()
    return visits

def get_visits_by_month(year: str, month: str):
    """
    Возвращает список посещений за указанный месяц.
    """
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT patients.full_name, services.name, services.price, visits.visit_date
        FROM visits
        JOIN patients ON visits.patient_id = patients.id
        JOIN services ON visits.service_id = services.id
        WHERE strftime('%Y', visits.visit_date) = ? AND strftime('%m', visits.visit_date) = ?
    ''', (year, month))
    visits = cursor.fetchall()
    conn.close()
    return visits