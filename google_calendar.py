from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# Если изменяете эти области доступа, удалите файл token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    """
    Аутентифицирует пользователя в Google Calendar API.
    """
    creds = None
    # Файл token.json хранит токены доступа пользователя и автоматически обновляется.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Если нет действительных учетных данных, пользователь входит в систему.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Сохраняем учетные данные для следующего запуска.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Создаем сервис для работы с Google Calendar API
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_event(calendar_service, summary, start_time, end_time, timezone='Europe/Moscow'):
    """Создание события в Google Calendar."""
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time,
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time,
            'timeZone': timezone,
        },
    }
    try:
        event = calendar_service.events().insert(
            calendarId='primary',
            body=event
        ).execute()
        return event.get('htmlLink')
    except Exception as e:
        raise Exception(f"Ошибка при создании события: {e}")