import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Monitor RDS Storage

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 076: Monitor RDS Storage")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "076",
            "name": "Monitor RDS Storage",
            "category": "rds",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
