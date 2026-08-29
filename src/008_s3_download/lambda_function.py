import os, json, boto3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket = event.get("bucket") or os.environ["BUCKET"]
    key = event["key"]
    obj = s3.get_object(Bucket=bucket, Key=key)
    return {"statusCode": 200, "body": json.dumps({
        "bucket": bucket, "key": key, "size": obj["ContentLength"], "content_type": obj.get("ContentType")
    })}
