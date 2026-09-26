import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Delete Unused EBS Volumes

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 036: Delete Unused EBS Volumes")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "036",
            "name": "Delete Unused EBS Volumes",
            "category": "ebs",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
