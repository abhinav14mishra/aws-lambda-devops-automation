import os, json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    ids = event.get("instance_ids") or [os.environ["INSTANCE_ID"]]
    result = ec2.terminate_instances(InstanceIds=ids)
    return {"statusCode": 200, "body": json.dumps({"terminated": ids, "result": result}, default=str)}
