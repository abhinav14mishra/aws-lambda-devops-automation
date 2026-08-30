import os, json, boto3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    source = event.get("source_bucket") or os.environ["SOURCE_BUCKET"]
    target = event.get("target_bucket") or os.environ["TARGET_BUCKET"]
    key = event["key"]
    s3.copy_object(Bucket=target, Key=key, CopySource={"Bucket": source, "Key": key})
    return {"statusCode": 200, "body": json.dumps({"copied": key, "from": source, "to": target})}
