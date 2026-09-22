import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Delete Old EBS Snapshots

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 032: Delete Old EBS Snapshots")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "032",
            "name": "Delete Old EBS Snapshots",
            "category": "ebs",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
