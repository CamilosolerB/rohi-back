import json
from src.services.history_service import UserService

def lambda_handler(event, context):
    print(event)
    service = UserService()
    route = event.get("routeKey", "")
    path_params = event.get("pathParameters", {})
    body = json.loads(event["body"]) if event.get("body") else {}

    try:
        if route == "GET /history/{documentId}":
            document_id = path_params.get("documentId")
            history = service.get_history(document_id)
            return {
                "statusCode": 200,
                "body": json.dumps(history.model_dump())
            }
        
        if route == "POST /history":
            history_dto = service.create_history(body)
            return {
                "statusCode": 201,
                "body": json.dumps(history_dto.model_dump())
            }
        if route == "PUT /history/{documentId}":
            document_id = path_params.get("documentId")
            updated_history = service.update_history(document_id, body)
            return {
                "statusCode": 200,
                "body": json.dumps(updated_history.model_dump())
            }
        if route == "DELETE /history/{documentId}":
            document_id = path_params.get("documentId")
            success = service.delete_history(document_id)
            return {
                "statusCode": 200 if success else 404,
                "body": json.dumps({"message": "History deleted" if success else "History not found"})
            }
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid route"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(e)})
        }
    