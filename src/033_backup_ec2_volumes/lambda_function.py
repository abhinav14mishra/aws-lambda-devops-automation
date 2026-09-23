import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Backup EC2 Volumes

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 033: Backup EC2 Volumes")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "033",
            "name": "Backup EC2 Volumes",
            "category": "ebs",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
