import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Detect Old IAM Access Keys

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 060: Detect Old IAM Access Keys")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "060",
            "name": "Detect Old IAM Access Keys",
            "category": "iam",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
