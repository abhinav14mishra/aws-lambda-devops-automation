import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Read CSV from S3

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 014: Read CSV from S3")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "014",
            "name": "Read CSV from S3",
            "category": "s3",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
