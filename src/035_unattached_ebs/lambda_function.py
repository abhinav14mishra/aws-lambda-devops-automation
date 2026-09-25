import json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    r = ec2.describe_volumes(Filters=[{"Name":"status","Values":["available"]}])
    volumes = [{"id":v["VolumeId"],"size_gb":v["Size"]} for v in r["Volumes"]]
    return {"statusCode":200,"body":json.dumps({"count":len(volumes),"volumes":volumes})}
