import pandas as pd
from datetime import datetime

def create_excel_report(data: list, filename: str):
    """
    Создает Excel-файл с отчетом на основе данных.
    :param data: Список данных для отчета.
    :param filename: Имя файла для сохранения.
    """
    # Преобразуем данные в DataFrame
    df = pd.DataFrame(data, columns=["ФИО пациента", "Услуга", "Цена", "Дата посещения"])

    # Сохраняем DataFrame в Excel-файл
    df.to_excel(filename, index=False)

def generate_report_day(date: str):
    """
    Генерирует отчет за указанный день.
    :param date: Дата в формате ГГГГ-ММ-ДД.
    :return: Имя файла с отчетом.
    """
    filename = f"report_day_{date}.xlsx"
    # Здесь можно добавить логику для получения данных из базы данных
    # Например: data = get_visits_by_day(date)
    return filename

def generate_report_month(year: str, month: str):
    """
    Генерирует отчет за указанный месяц.
    :param year: Год в формате ГГГГ.
    :param month: Месяц в формате ММ.
    :return: Имя файла с отчетом.
    """
    filename = f"report_month_{year}-{month}.xlsx"
    # Здесь можно добавить логику для получения данных из базы данных
    # Например: data = get_visits_by_month(year, month)
    return filename