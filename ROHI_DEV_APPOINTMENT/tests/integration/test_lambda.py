import json
from ROHI_DEV_USER.lambda_function import lambda_handler

def test_lambda_login():
    # Simular evento de API Gateway v2
    event = {
        "version": "2.0",
        "routeKey": "POST /user/log_in",
        "rawPath": "/user/log_in",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "content-type": "application/json",
            "host": "ka1ia73m47.execute-api.us-east-1.amazonaws.com",
            "user-agent": "PostmanRuntime/7.48.0"
        },
        "requestContext": {
            "http": {
                "method": "POST",
                "path": "/user/log_in",
                "protocol": "HTTP/1.1",
                "sourceIp": "190.145.240.185",
                "userAgent": "PostmanRuntime/7.48.0"
            }
        },
        "body": json.dumps({
            "fullname": "Camilo Soler",
            "email": "caansobu2@gmail.com",
            "documentId": "1070942659",
            "phoneNumber": "3054002437"
        }),
        "isBase64Encoded": False
    }

    context = {}  # En test no necesitas contexto real
    response = lambda_handler(event, context)

    print("Response:", response)
    assert response["statusCode"] == 200  # ejemplo
