import json
from src.utilities.db import SessionLocal
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService
from src.dto.user_dto import UserDTO

def lambda_handler(event, context):
    db = SessionLocal()
    repo = UserRepository(db)
    service = UserService(repo)

    try:
        method = event.get("httpMethod")
        if method == "GET":
            user_id = event["pathParameters"]["id"]
            user = service.get_user(user_id)
            if not user:
                return {"statusCode": 404, "body": json.dumps({"message": "User not found"})}
            return {"statusCode": 200, "body": json.dumps(user.__dict__)}

        elif method == "POST":
            body = json.loads(event["body"])
            dto = UserDTO(**body)
            created = service.create_user(dto)
            return {"statusCode": 201, "body": json.dumps(created.__dict__)}

        elif method == "DELETE":
            user_id = event["pathParameters"]["id"]
            service.delete_user(user_id)
            return {"statusCode": 204, "body": json.dumps({"message": "User deleted"})}

        return {"statusCode": 400, "body": json.dumps({"message": "Unsupported method"})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
    finally:
        db.close()
