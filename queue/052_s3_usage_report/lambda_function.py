import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    S3 Storage Usage Report

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 052: S3 Storage Usage Report")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "052",
            "name": "S3 Storage Usage Report",
            "category": "s3",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
