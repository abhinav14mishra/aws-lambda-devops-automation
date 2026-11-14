import json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    ids = event.get("instance_ids", [])
    if not ids and event.get("detail",{}).get("instance-id"):
        ids=[event["detail"]["instance-id"]]
    if ids:
        ec2.reboot_instances(InstanceIds=ids)
    return {"statusCode":200,"body":json.dumps({"rebooted":ids})}
