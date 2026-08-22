import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Scheduled EC2 Start

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 025: Scheduled EC2 Start")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "025",
            "name": "Scheduled EC2 Start",
            "category": "ec2",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
