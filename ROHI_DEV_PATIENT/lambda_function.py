import json
from ROHI_DEV_PATIENT.src.dto.patient_dto import PatientCreateDTO, PatientResponseDTO
from ROHI_DEV_PATIENT.src.services.patient_service import PatientService

service = PatientService()

def lambda_handler(event, context):
    try:
        http_method = event.get("httpMethod")
        path = event.get("path", "")
        path_params = event.get("pathParameters") or {}
        body = json.loads(event.get("body", "{}")) if event.get("body") else {}

        if http_method == "POST" and path.endswith("/patient"):
            patient = service.create_patient(body)
            return {
                "statusCode": 201,
                "body": patient.json()
            }

        elif http_method == "GET" and path_params.get("id"):
            patient = service.get_patient(int(path_params["id"]))
            if not patient:
                return {"statusCode": 404, "body": json.dumps({"error": "Patient not found"})}
            return {
                "statusCode": 200,
                "body": patient.json()
            }

        elif http_method == "PUT" and path_params.get("id"):
            patient = service.update_patient(int(path_params["id"]), body)
            if not patient:
                return {"statusCode": 404, "body": json.dumps({"error": "Patient not found"})}
            return {
                "statusCode": 200,
                "body": patient.json()
            }

        elif http_method == "DELETE" and path_params.get("id"):
            deleted = service.delete_patient(int(path_params["id"]))
            if not deleted:
                return {"statusCode": 404, "body": json.dumps({"error": "Patient not found"})}
            return {
                "statusCode": 204,
                "body": ""
            }

        return {"statusCode": 400, "body": json.dumps({"error": "Invalid request"})}

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
