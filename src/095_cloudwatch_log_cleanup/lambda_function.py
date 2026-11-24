import os, json, boto3
logs = boto3.client("logs")

def lambda_handler(event, context):
    days = int(event.get("retention_days", os.environ.get("RETENTION_DAYS","30")))
    groups = logs.describe_log_groups().get("logGroups",[])
    updated=[]
    for g in groups:
        if g.get("retentionInDays") is None:
            logs.put_retention_policy(logGroupName=g["logGroupName"], retentionInDays=days)
            updated.append(g["logGroupName"])
    return {"statusCode":200,"body":json.dumps({"retention_days":days,"updated":updated})}
