from httpx import Request

# def handler(request: Request):
#     return {
#         "statusCode": 200,
#         "body": "Hello, World!"
#     }

def handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello, World!"
    }
