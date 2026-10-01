import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    S3 Image Thumbnail Generator

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 041: S3 Image Thumbnail Generator")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "041",
            "name": "S3 Image Thumbnail Generator",
            "category": "s3",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
