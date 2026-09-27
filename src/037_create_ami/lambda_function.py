import os, json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    iid = event.get("instance_id") or os.environ["INSTANCE_ID"]
    name = event.get("name") or os.environ.get("AMI_NAME","lambda-backup")
    r = ec2.create_image(InstanceId=iid, Name=name, NoReboot=True)
    return {"statusCode":200,"body":json.dumps({"image_id":r["ImageId"],"instance_id":iid})}
