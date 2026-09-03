import os, json, boto3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket = event.get("bucket") or os.environ["BUCKET"]
    key = event["key"]
    expires = int(event.get("expires", 900))
    url = s3.generate_presigned_url("get_object", Params={"Bucket": bucket, "Key": key}, ExpiresIn=expires)
    return {"statusCode": 200, "body": json.dumps({"url": url, "expires_in": expires})}
