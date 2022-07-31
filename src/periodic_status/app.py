from datetime import datetime
import json
import boto3
import os
import random
from utils.models import PingData
from utils.consts import SNS_QUEUE_ARN_ENV

sns = boto3.resource("sns")
topic = sns.Topic(os.environ.get(SNS_QUEUE_ARN_ENV))


def lambda_handler(event, context):
    print("About to send status update message")
    if random.choice(range(1,10)) == 10:
        topic.publish(Message=json.dumps({"exact_time": -1}))
    else:
        topic.publish(Message=PingData().to_json())
    print(f"Message sent successfully to '{topic.arn}'")
