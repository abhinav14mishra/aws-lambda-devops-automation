import json, boto3
iam = boto3.client("iam")

def lambda_handler(event, context):
    paginator = iam.get_paginator("list_users")
    users = [u["UserName"] for p in paginator.paginate() for u in p["Users"]]
    return {"statusCode":200,"body":json.dumps({"users":users})}
