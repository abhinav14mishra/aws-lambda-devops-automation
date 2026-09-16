import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Detect Idle EC2 Instances

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 026: Detect Idle EC2 Instances")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "026",
            "name": "Detect Idle EC2 Instances",
            "category": "ec2",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
