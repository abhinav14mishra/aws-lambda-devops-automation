import os, json, boto3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket = event.get("bucket") or os.environ["BUCKET"]
    prefix = event.get("prefix", "")
    paginator = s3.get_paginator("list_objects_v2")
    keys = []
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        keys.extend(x["Key"] for x in page.get("Contents", []))
    return {"statusCode": 200, "body": json.dumps({"count": len(keys), "keys": keys})}
