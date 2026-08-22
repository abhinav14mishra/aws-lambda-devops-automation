import os, json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    ids = event.get("instance_ids", [])
    key = event.get("tag_key", os.environ.get("TAG_KEY", "ManagedBy"))
    value = event.get("tag_value", os.environ.get("TAG_VALUE", "Lambda"))
    if not ids:
        r = ec2.describe_instances(Filters=[{"Name":"instance-state-name","Values":["pending","running","stopping","stopped"]}])
        ids = [i["InstanceId"] for x in r["Reservations"] for i in x["Instances"]]
    if ids:
        ec2.create_tags(Resources=ids, Tags=[{"Key": key, "Value": value}])
    return {"statusCode":200,"body":json.dumps({"tagged":ids,"tag":{key:value}})}
