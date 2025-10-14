import json
from src.services.user_service import UserService

def lambda_handler(event, context):
    print(event)
    service = UserService()
    route = event.get("routeKey", "")
    path_params = event.get("pathParameters", {})
    body = json.loads(event["body"]) if event.get("body") else {}

    if route == "POST /user/log_in":
        user = service.get_user_by_email(body["email"])
        return {"statusCode": 200, "body": json.dumps(user.model_dump())}

    if route == "POST /user/sign_in":
        user = service.create_user(body)
        return {"statusCode": 201, "body": json.dumps(user.model_dump())}
    
    if route == "GET /user/{documentId}":
        document_id = path_params.get("documentId")
        user = service.get_user(document_id)
        return {"statusCode": 200, "body": json.dumps(user.model_dump())}
    
    if route == "PUT /user/{documentId}":
        document_id = path_params.get("documentId")
        user = service.update_user(document_id, **body)
        return {"statusCode": 200, "body": json.dumps(user.model_dump())}
    
    if route == "DELETE /user/{documentId}":
        document_id = path_params.get("documentId")
        service.delete_user(document_id)
        return {"statusCode": 200, "body": json.dumps({"message": "User deleted successfully"})}
    
    return {"statusCode": 404, "body": json.dumps({"error": "Route not found"})}
