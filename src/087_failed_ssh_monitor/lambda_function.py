import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Monitor Failed SSH Attempts

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 087: Monitor Failed SSH Attempts")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "087",
            "name": "Monitor Failed SSH Attempts",
            "category": "monitoring",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
