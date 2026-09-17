import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    EC2 Status Report

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 027: EC2 Status Report")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "027",
            "name": "EC2 Status Report",
            "category": "ec2",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
