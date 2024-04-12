from typing import Any


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    print(f"Received event: {event}")

    return {"statusCode": 200, "body": "Hello from Lambda!"}
