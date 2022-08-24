from datetime import datetime
import json
import boto3
import os
import random
from utils.models import PingData
from utils.consts import SNS_QUEUE_ARN_ENV
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

sns = boto3.resource("sns")
topic = sns.Topic(os.environ.get(SNS_QUEUE_ARN_ENV))


def lambda_handler(event, context):
    print("About to send status update message")
    message = PingData().to_json()
    if random.randint(1,10) == 10:
        message = {"exact_time": str(datetime.now().timestamp())}
        topic.publish(Message=json.dumps(message))
    else:
        topic.publish(Message=message)
        topic.publish(Message=message)
    print(f"Message sent successfully to '{topic.arn}'")
    print(json.dumps(message, indent=2))
