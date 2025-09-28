import json
from src.dto.user_dto import UserCreateDTO
from src.services.user_service import UserService

def lambda_handler(event, context):
    body = json.loads(event["body"])
    service = UserService()

    user = service.create_user(body)

    return {
        "statusCode": 201,
        "body": user.json()
    }
