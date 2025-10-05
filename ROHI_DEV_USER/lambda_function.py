import json
from src.services.user_service import UserService

def lambda_handler(event, context):
    print(event)
    body = json.loads(event["body"])
    service = UserService()
    if event["routeKey"] == "POST /user/sign_in":
        user = service.create_user(body)
        return {"statusCode": 201, "body": json.dumps(user)}
    
    if event["routeKey"] == "POST /user/log_in":
        user = service.login_user(body)
        return {"statusCode": 200, "body": json.dumps(user)}
    
    return {"statusCode": 404, "body": json.dumps({"error": "Route not found"})}
