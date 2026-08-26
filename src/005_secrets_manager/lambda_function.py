import os, json, boto3
client = boto3.client("secretsmanager")

def lambda_handler(event, context):
    secret_id = event.get("secret_id") or os.environ["SECRET_ID"]
    value = client.get_secret_value(SecretId=secret_id)
    # Return metadata by default; avoid exposing secrets in production responses/logs.
    return {"statusCode": 200, "body": json.dumps({
        "secret_id": secret_id,
        "has_secret_string": bool(value.get("SecretString")),
        "has_secret_binary": bool(value.get("SecretBinary"))
    })}
