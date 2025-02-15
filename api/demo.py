from httpx import Request

def handler(request: Request):
    return {
        "statusCode": 200,
        "body": "Hello, World!"
    }
