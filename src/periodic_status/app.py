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
    if random.randint(1,10) == 10:
        topic.publish(Message=json.dumps({"exact_time": str(datetime.now().timestamp())}))
    else:
        topic.publish(Message=PingData().to_json())
        topic.publish(Message=PingData().to_json())
        topic.publish(Message=PingData().to_json())
    print(f"Message sent successfully to '{topic.arn}'")
