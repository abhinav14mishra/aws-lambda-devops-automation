import os, json, boto3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    source = event.get("source_bucket") or os.environ["SOURCE_BUCKET"]
    archive = event.get("archive_bucket") or os.environ["ARCHIVE_BUCKET"]
    key = event["key"]
    s3.copy_object(Bucket=archive, Key=key, CopySource={"Bucket":source,"Key":key}, StorageClass="GLACIER")
    s3.delete_object(Bucket=source, Key=key)
    return {"statusCode":200,"body":json.dumps({"archived":key})}
