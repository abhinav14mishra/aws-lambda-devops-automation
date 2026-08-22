import os, json, time, boto3
rds = boto3.client("rds")

def lambda_handler(event, context):
    db = event.get("db_instance_id") or os.environ["DB_INSTANCE_ID"]
    sid = event.get("snapshot_id") or f"{db}-{int(time.time())}"
    r = rds.create_db_snapshot(DBSnapshotIdentifier=sid, DBInstanceIdentifier=db)
    return {"statusCode":200,"body":json.dumps({"snapshot_id":r["DBSnapshot"]["DBSnapshotIdentifier"]})}
