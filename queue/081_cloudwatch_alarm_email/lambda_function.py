import os, json, boto3
sns = boto3.client("sns")

def lambda_handler(event, context):
    topic = event.get("topic_arn") or os.environ["SNS_TOPIC_ARN"]
    message = event.get("message", "CloudWatch alarm notification")
    r = sns.publish(TopicArn=topic, Subject="AWS Alarm", Message=json.dumps(message, default=str))
    return {"statusCode":200,"body":json.dumps({"message_id":r["MessageId"]})}
