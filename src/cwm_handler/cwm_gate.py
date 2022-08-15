
from decimal import Decimal
import boto3
import json
import os
from utils.models import PingData
from utils.consts import CWM_KILL_SWITCH_ENV,DDB_NAME_ENV
import random
import string

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ[DDB_NAME_ENV])

def lambda_handler(event, context):
    if os.environ.get(CWM_KILL_SWITCH_ENV) in ["true", "True"]:
        print("Stopped sending message to DDB")
    else:
        print("Sending to DDB")
        body = json.loads(event["Records"][0]["body"])
        table.put_item(Item={"id": get_random_id(), "time":Decimal(PingData.from_json(body["Message"]).exact_time.timestamp())})


def get_random_id() -> str:
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))

