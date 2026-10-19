import json, boto3
iam = boto3.client("iam")

def lambda_handler(event, context):
    username = event["username"]
    keys = iam.list_access_keys(UserName=username)["AccessKeyMetadata"]
    created = []
    for key in keys:
        if key["Status"] == "Active":
            iam.update_access_key(UserName=username, AccessKeyId=key["AccessKeyId"], Status="Inactive")
    r = iam.create_access_key(UserName=username)
    created.append(r["AccessKey"]["AccessKeyId"])
    return {"statusCode":200,"body":json.dumps({"new_access_key_ids":created})}
