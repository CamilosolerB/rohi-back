import json
from src.services.appointment_service import AppointmentService

def lambda_handler(event, context):
    print(event)
    service = AppointmentService()
    route = event.get("routeKey", "")
    path_params = event.get("pathParameters", {})
    body = json.loads(event["body"]) if event.get("body") else {}

    try:
        if route == "GET /appointments/free":
            appointments = service.get_appointments_free()
            return {
                "statusCode": 200,
                "body": json.dumps([appointment.model_dump() for appointment in appointments])
            }
        if route == "GET /appointments/professional/{professionalId}":
            professional_id = int(path_params.get("professionalId"))
            appointments = service.get_appointments_by_professional(professional_id)
            return {
                "statusCode": 200,
                "body": json.dumps([appointment.model_dump() for appointment in appointments])
            }
        if route == "GET /appointments/patient/{patientId}":
            patient_id = int(path_params.get("patientId"))
            appointments = service.get_appointments_by_patient(patient_id)
            return {
                "statusCode": 200,
                "body": json.dumps([appointment.model_dump() for appointment in appointments])
            }
        if route == "PUT /appointments/{appointmentId}/status":
            appointment_id = int(path_params.get("appointmentId"))
            new_status = body.get("new_status")
            appointment = service.update_appointment_status(appointment_id, new_status)
            return {
                "statusCode": 200,
                "body": json.dumps(appointment.model_dump())
            }
        if route == "GET /appointments/{appointmentId}":
            appointment_id = int(path_params.get("appointmentId"))
            appointment = service.get_appointment_by_id(appointment_id)
            return {
                "statusCode": 200,
                "body": json.dumps(appointment.model_dump())
            }
        if route == "POST /appointments":
            appointment = service.create_appointment(body)
            return {
                "statusCode": 201,
                "body": json.dumps(appointment.model_dump())
            }
        if route == "DELETE /appointments/{appointmentId}":
            appointment_id = int(path_params.get("appointmentId"))
            service.delete_appointment(appointment_id)
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Appointment deleted successfully"})
            }
        
        if route == "GET /appointments":
            appointments = service.get_all_appointments()
            return {
                "statusCode": 200,
                "body": json.dumps([appointment.model_dump() for appointment in appointments])
            }
        
        if route == "PUT /appointments/{appointmentId}":
            appointment_id = int(path_params.get("appointmentId"))
            appointment = service.update_appointment(appointment_id, **body)
            return {
                "statusCode": 200,
                "body": json.dumps(appointment.model_dump())
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
