import os, json, base64, boto3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket = event.get("bucket") or os.environ["BUCKET"]
    key = event["key"]
    body = base64.b64decode(event["body"]) if event.get("is_base64") else event["body"].encode()
    s3.put_object(Bucket=bucket, Key=key, Body=body, ServerSideEncryption="AES256")
    return {"statusCode": 200, "body": json.dumps({"bucket": bucket, "key": key})}
