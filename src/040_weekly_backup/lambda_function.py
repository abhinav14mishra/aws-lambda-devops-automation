import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Weekly AWS Backup

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 040: Weekly AWS Backup")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "040",
            "name": "Weekly AWS Backup",
            "category": "backup",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
