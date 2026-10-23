import json, boto3
iam = boto3.client("iam")

def lambda_handler(event, context):
    users = iam.list_users()["Users"]
    findings=[]
    for u in users:
        name=u["UserName"]
        try:
            iam.get_user(UserName=name)
            iam.list_mfa_devices(UserName=name)
            if not iam.list_mfa_devices(UserName=name).get("MFADevices"):
                findings.append(name)
        except Exception:
            pass
    return {"statusCode":200,"body":json.dumps({"users_without_mfa":findings})}
