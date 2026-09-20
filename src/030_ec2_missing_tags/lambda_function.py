import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Find EC2 Missing Tags

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 030: Find EC2 Missing Tags")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "030",
            "name": "Find EC2 Missing Tags",
            "category": "ec2",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
