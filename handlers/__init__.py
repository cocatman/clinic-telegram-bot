from .start import register_start_handlers
from .add_patient import register_add_patient_handlers
from .add_service import register_add_service_handlers
from .add_visit import register_add_visit_handlers
from .find_patient import register_find_patient_handlers
from .edit_patient import register_edit_patient_handlers
from .patient_visits import register_patient_visits_handlers
from .all_visits import register_all_visits_handlers
from .reports import register_reports_handlers
from .list_services import register_list_services_handlers

def register_handlers(dp):
    """
    Регистрирует все обработчики.
    """
    register_start_handlers(dp)
    register_add_patient_handlers(dp)
    register_add_service_handlers(dp)
    register_add_visit_handlers(dp)
    register_find_patient_handlers(dp)
    register_edit_patient_handlers(dp)
    register_patient_visits_handlers(dp)
    register_all_visits_handlers(dp)
    register_reports_handlers(dp)
    register_list_services_handlers(dp)