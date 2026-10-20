# Day 60 — Detect Old IAM Access Keys

## Objective

Build and understand a practical AWS Lambda automation pattern for **Detect Old IAM Access Keys**.

## Files

- `lambda_function.py` — Lambda handler
- `test_event.json` — starter test payload
- `requirements.txt` — Python dependency declaration

## Typical AWS components

- AWS Lambda
- Python
- boto3
- CloudWatch Logs
- IAM execution role
- EventBridge/S3/API Gateway/SNS/SQS as appropriate

## Configuration

Check `lambda_function.py` for environment variables and event fields required by this project.

## IAM

Grant only the API actions required by this function. Start with a narrow policy and expand it only when CloudTrail/CloudWatch or Lambda errors show a genuine missing permission.

## Production hardening

Before treating this as production-ready, add:

- input validation
- pagination
- retry/backoff for transient AWS errors
- idempotency
- structured logging
- CloudWatch alarms
- timeout/memory tuning
- dead-letter handling where appropriate
- least-privilege IAM
- unit tests/mocks
- safe handling of destructive operations

## Day 60 challenge

Be able to explain:

1. What event triggers this Lambda?
2. Which boto3 APIs are used?
3. What IAM permissions are required?
4. What happens when the AWS API fails?
5. How would you monitor it in production?
6. How would you deploy it with Terraform or AWS SAM?
