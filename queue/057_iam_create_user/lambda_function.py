import os, json, boto3
iam = boto3.client("iam")

def lambda_handler(event, context):
    username = event.get("username") or os.environ["USERNAME"]
    r = iam.create_user(UserName=username)
    return {"statusCode":200,"body":json.dumps({"user":r["User"]["UserName"]})}
