import os, json, boto3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket = event.get("bucket") or os.environ["BUCKET"]
    key = event["key"]
    s3.delete_object(Bucket=bucket, Key=key)
    return {"statusCode": 200, "body": json.dumps({"deleted": key})}
