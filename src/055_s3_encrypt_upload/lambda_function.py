import os, json, boto3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket = event.get("bucket") or os.environ["BUCKET"]
    key = event["key"]
    s3.copy_object(Bucket=bucket, Key=key, CopySource={"Bucket":bucket,"Key":key},
                   ServerSideEncryption="AES256", MetadataDirective="COPY")
    return {"statusCode":200,"body":json.dumps({"encrypted":key})}
