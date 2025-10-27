import json
from src.services.receipt_service import ReceiptService

def lambda_handler(event, context):
    print(event)
    service = ReceiptService()
    route = event.get("routeKey", "")
    path_params = event.get("pathParameters", {})
    body = json.loads(event["body"]) if event.get("body") else {}

    try:
        if route == "POST /receipts":
            patient_email = body.get("patient_email", "")
            receipt = service.create_receipt(body, patient_email)
            return {
                "statusCode": 201,
                "body": json.dumps(receipt)
            }
        elif route == "GET /receipts/{receipt_id}":
            receipt_id = int(path_params.get("receipt_id", 0))
            receipt = service.get_receipt(receipt_id)
            return {
                "statusCode": 200,
                "body": json.dumps(receipt)
            }
        elif route == "GET /receipts":
            receipts = service.get_all_receipts()
            return {
                "statusCode": 200,
                "body": json.dumps(receipts)
            }
        elif route == "PUT /receipts/{receipt_id}":
            receipt_id = int(path_params.get("receipt_id", 0))
            receipt = service.update_receipt(receipt_id, **body)
            return {
                "statusCode": 200,
                "body": json.dumps(receipt)
            }
        elif route == "DELETE /receipts/{receipt_id}":
            receipt_id = int(path_params.get("receipt_id", 0))
            service.delete_receipt(receipt_id)
            return {
                "statusCode": 204,
                "body": ""
            }
        elif route == "POST /receipts/complete-payment":
            receipt = service.complete_receipt_payment(body)
            return {
                "statusCode": 200,
                "body": json.dumps(receipt)
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Route not found"})
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(e)})
        }