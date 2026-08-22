import os, json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    volume_id = event.get("volume_id") or os.environ["VOLUME_ID"]
    r = ec2.create_snapshot(VolumeId=volume_id, Description="Lambda automated EBS snapshot")
    return {"statusCode":200,"body":json.dumps({"snapshot_id":r["SnapshotId"],"volume_id":volume_id})}
