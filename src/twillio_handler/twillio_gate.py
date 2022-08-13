import boto3
import json
import os
from utils.models import PingData
from utils.consts import TWILLIO_KILL_SWITCH_ENV, KINESIS_NAME_ENV
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

kinesis = boto3.client("kinesis")


def lambda_handler(event, context):
    if os.environ.get(TWILLIO_KILL_SWITCH_ENV) in ["true", "True"]:
        print("Stopped sending message to twillio")
    else:
        print("Sending to Kinesis")
        body = json.loads(event["Records"][0]["body"])
        kinesis.put_record(
            StreamName=os.environ.get(KINESIS_NAME_ENV),
            Data=body["Message"],
            PartitionKey=body["Message"],
        )
