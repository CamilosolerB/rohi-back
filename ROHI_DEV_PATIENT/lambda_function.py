import json
from src.services.patient_service import PatientService

service = PatientService()

def lambda_handler(event, context):
    try:
        print(event)
        service = PatientService()
        route = event.get("routeKey", "")
        path_params = event.get("pathParameters", {})
        body = json.loads(event["body"]) if event.get("body") else {}

        if route == "POST /patients":
            patient = service.create_patient(body)
            return {
                "statusCode": 201,
                "body": json.dumps(patient.model_dump())
            }
        
        if route == "GET /patients":
            patients = service.list_patients()
            patients_json = [json.loads(patient.model_dump_json()) for patient in patients]
            return {
                "statusCode": 200,
                "body": json.dumps(patients_json)
            }
        
        if route == "GET /patients/{documentId}":
            document_id = path_params.get("documentId")
            patient = service.get_patient(document_id)
            return {
                "statusCode": 200,
                "body": json.dumps(patient.model_dump())
            }
        
        if route == "PUT /patients/{documentId}":
            document_id = path_params.get("documentId")
            patient = service.update_patient(document_id, **body)
            return {
                "statusCode": 200,
                "body": json.dumps(patient.model_dump())
            }
        
        if route == "DELETE /patients/{documentId}":
            document_id = path_params.get("documentId")
            service.delete_patient(document_id)
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Patient deleted successfully"})
            }
        
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Route not found"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
