import json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    addresses = ec2.describe_addresses()["Addresses"]
    unused = [a.get("AllocationId") for a in addresses if not a.get("InstanceId") and not a.get("NetworkInterfaceId")]
    return {"statusCode":200,"body":json.dumps({"unused_allocation_ids":unused})}
