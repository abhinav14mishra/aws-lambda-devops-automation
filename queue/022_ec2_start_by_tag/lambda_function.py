import os, json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    key = event.get("tag_key", os.environ.get("TAG_KEY", "Environment"))
    value = event.get("tag_value", os.environ.get("TAG_VALUE", "dev"))
    r = ec2.describe_instances(Filters=[{"Name": f"tag:{key}", "Values": [value]}, {"Name": "instance-state-name", "Values": ["stopped"]}])
    ids = [i["InstanceId"] for res in r["Reservations"] for i in res["Instances"]]
    if ids:
        ec2.start_instances(InstanceIds=ids)
    return {"statusCode": 200, "body": json.dumps({"started": ids})}
