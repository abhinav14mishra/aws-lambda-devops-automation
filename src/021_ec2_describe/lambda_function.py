import json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    paginator = ec2.get_paginator("describe_instances")
    instances = []
    for page in paginator.paginate():
        for res in page["Reservations"]:
            for i in res["Instances"]:
                instances.append({"id": i["InstanceId"], "state": i["State"]["Name"], "type": i["InstanceType"]})
    return {"statusCode": 200, "body": json.dumps({"count": len(instances), "instances": instances})}
