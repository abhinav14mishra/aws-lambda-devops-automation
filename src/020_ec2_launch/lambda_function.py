import os, json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    image_id = event.get("image_id") or os.environ["AMI_ID"]
    instance_type = event.get("instance_type", os.environ.get("INSTANCE_TYPE", "t3.micro"))
    subnet_id = event.get("subnet_id") or os.environ["SUBNET_ID"]
    sg_id = event.get("security_group_id") or os.environ["SECURITY_GROUP_ID"]
    r = ec2.run_instances(ImageId=image_id, InstanceType=instance_type, MinCount=1, MaxCount=1,
                           SubnetId=subnet_id, SecurityGroupIds=[sg_id])
    iid = r["Instances"][0]["InstanceId"]
    return {"statusCode": 200, "body": json.dumps({"instance_id": iid})}
