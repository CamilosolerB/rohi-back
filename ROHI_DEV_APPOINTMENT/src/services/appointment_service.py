from src.dto.appointment_dto import AppointmentDTO
from src.repositories.appointment_repository import AppointmentRepository
from src.utilities.db_appointment import get_session

class AppointmentService:
    def __init__(self):
        self.db = get_session()
        self.repo = AppointmentRepository(self.db)

    def get_appointments_free(self):
        appointments = self.repo.get_appointments_free()
        return [ AppointmentDTO.from_orm(appointment) for appointment in appointments ]
    
    def get_appointments_by_professional(self, professional_id: int):
        appointments = self.repo.get_appointments_by_professional(professional_id)
        return [ AppointmentDTO.from_orm(appointment) for appointment in appointments ]

    def get_appointments_by_patient(self, patient_id: int):
        appointments = self.repo.get_appointments_by_patient(patient_id)
        return [ AppointmentDTO.from_orm(appointment) for appointment in appointments ]

    def update_appointment_status(self, appointment_id: int, new_status) :
        appointment = self.repo.update_appointment_status(appointment_id, new_status)
        return AppointmentDTO.from_orm(appointment)

    def get_appointment_by_id(self, appointment_id: int):
        appointment = self.repo.get_appointment_by_id(appointment_id)
        return AppointmentDTO.from_orm(appointment)

    def create_appointment(self, body):
        appointment = self.repo.create_appointment(body)
        return AppointmentDTO.from_orm(appointment)

    def delete_appointment(self, appointment_id: int):
        appointment = self.repo.delete_appointment(appointment_id)
        return AppointmentDTO.from_orm(appointment)

    def get_all_appointments(self):
        appointments = self.repo.get_all_appointments()
        return [ AppointmentDTO.from_orm(appointment) for appointment in appointments ]

    def update_appointment(self, appointment_id: int, **kwargs):
        appointment = self.repo.update_appointment(appointment_id, **kwargs)
        return AppointmentDTO.from_orm(appointment)

    
