from src.models.appointmen_model import Appointment, AppointmentStatus
from sqlalchemy.orm import Session

class AppointmentRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_appointments_free(self):
        return self.session.query(Appointment).filter(Appointment.status == AppointmentStatus.FREE).all()
    
    def get_appointments_by_professional(self, professional_id: int):
        return self.session.query(Appointment).filter(Appointment.professional_id == professional_id).all()
    
    def get_appointments_by_patient(self, patient_id: int):
        return self.session.query(Appointment).filter(Appointment.patient_id == patient_id).all()
    
    def update_appointment_status(self, appointment_id: int, new_status: AppointmentStatus) -> Appointment | None:
        appointment = self.session.query(Appointment).filter(Appointment.id == appointment_id).first()
        if not appointment:
            return None
        appointment.status = new_status
        self.session.commit()
        self.session.refresh(appointment)
        return appointment

    def get_appointment_by_id(self, appointment_id: int):
        return self.session.query(Appointment).filter(Appointment.id == appointment_id).first()
    
    def create_appointment(self, body) -> Appointment:
        appointment = Appointment(**body)
        self.session.add(appointment)
        self.session.commit()
        self.session.refresh(appointment)
        return appointment
    
    def delete_appointment(self, appointment_id: int) -> Appointment | None:
        appointment = self.get_appointment_by_id(appointment_id)
        if not appointment:
            return None
        self.session.delete(appointment)
        self.session.commit()
        return appointment
    
    def get_all_appointments(self) -> list[Appointment]:
        return self.session.query(Appointment).all()
    
    def update_appointment(self, appointment_id: int, **kwargs) -> Appointment | None:
        appointment = self.get_appointment_by_id(appointment_id)
        if not appointment:
            return None
        for key, value in kwargs.items():
            if hasattr(appointment, key) and value is not None:
                setattr(appointment, key, value)
        self.session.commit()
        self.session.refresh(appointment)
        return appointment
    
    