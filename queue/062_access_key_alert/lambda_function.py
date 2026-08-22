import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Access Key Expiry Alert

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 062: Access Key Expiry Alert")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "062",
            "name": "Access Key Expiry Alert",
            "category": "iam",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
