import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Stop Idle Resources For Cost Saving

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 091: Stop Idle Resources For Cost Saving")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "091",
            "name": "Stop Idle Resources For Cost Saving",
            "category": "cost",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
