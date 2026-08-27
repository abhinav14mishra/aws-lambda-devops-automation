import os, json, boto3
ssm = boto3.client("ssm")

def lambda_handler(event, context):
    name = event.get("name") or os.environ["PARAMETER_NAME"]
    value = ssm.get_parameter(Name=name, WithDecryption=True)
    return {"statusCode": 200, "body": json.dumps({"name": name, "value": value["Parameter"]["Value"]})}
