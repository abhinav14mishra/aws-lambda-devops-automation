import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Monitor Memory Metric

    This project is intentionally a safe, interview-friendly implementation
    pattern. Add the AWS API calls for your target environment and grant only
    the required IAM permissions.
    """
    logger.info("Running 084: Monitor Memory Metric")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "project": "084",
            "name": "Monitor Memory Metric",
            "category": "monitoring",
            "next_step": "Configure the documented AWS resources and least-privilege IAM role."
        })
    }
