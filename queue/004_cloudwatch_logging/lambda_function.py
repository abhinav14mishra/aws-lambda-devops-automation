import json, logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event, default=str))
    return {"statusCode": 200, "body": json.dumps({"logged": True})}
