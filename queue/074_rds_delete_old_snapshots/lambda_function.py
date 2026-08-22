import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Delete Old RDS Snapshots

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 074: Delete Old RDS Snapshots")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "074",
            "name": "Delete Old RDS Snapshots",
            "category": "rds",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
