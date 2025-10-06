import json
from src.services.professional_service import ProfessionalService

service = ProfessionalService()

def lambda_handler(event, context):
    try:
        print(event)
        service = ProfessionalService()
        route = event.get("routeKey", "")
        path_params = event.get("pathParameters", {})
        body = json.loads(event["body"]) if event.get("body") else {}

        if route == "POST /professional":
            patient = service.create_professional(body)
            return {
                "statusCode": 201,
                "body": json.dumps(patient.model_dump())
            }
        
        if route == "GET /professional":
            professionals = service.list_professionals()
            professionals_json = [json.loads(professional.model_dump_json()) for professional in professionals]
            return {
                "statusCode": 200,
                "body": json.dumps(professionals_json)
            }
        
        if route == "GET /professional/{documentId}":
            document_id = path_params.get("documentId")
            professional = service.get_professional(document_id)
            return {
                "statusCode": 200,
                "body": json.dumps(professional.model_dump())
            }
        
        if route == "PUT /professional/{documentId}":
            document_id = path_params.get("documentId")
            professional = service.update_professional(document_id, **body)
            return {
                "statusCode": 200,
                "body": json.dumps(professional.model_dump())
            }
        
        if route == "DELETE /professional/{documentId}":
            document_id = path_params.get("documentId")
            service.delete_professional(document_id)
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Professional deleted successfully"})
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
