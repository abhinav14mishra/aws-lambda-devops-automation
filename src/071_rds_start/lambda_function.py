import os, json, boto3
rds = boto3.client("rds")

def lambda_handler(event, context):
    db = event.get("db_instance_id") or os.environ["DB_INSTANCE_ID"]
    r = rds.start_db_instance(DBInstanceIdentifier=db)
    return {"statusCode":200,"body":json.dumps({"db":db,"status":r["DBInstance"]["DBInstanceStatus"]})}
