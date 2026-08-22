import os, json, boto3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket = event.get("bucket") or os.environ["BUCKET"]
    r = s3.put_public_access_block(Bucket=bucket, PublicAccessBlockConfiguration={
        "BlockPublicAcls": True, "IgnorePublicAcls": True, "BlockPublicPolicy": True, "RestrictPublicBuckets": True
    })
    return {"statusCode":200,"body":json.dumps({"bucket":bucket,"blocked":True,"request_id":r["ResponseMetadata"]["RequestId"]})}
