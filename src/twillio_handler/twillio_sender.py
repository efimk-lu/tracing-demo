import os
from twilio.rest import Client
import base64
from utils.models import PingData
from utils.consts import TWILLIO_SECRET_MANAGER_KEY_ENV
from functools import cache
import boto3
import json
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

def lambda_handler(event, context):
    ping = base64.b64decode(event["Records"][0]["kinesis"]["data"])
    secret = get_secret()
    account_sid = secret["twillio_account_sid"]
    auth_token = secret["twillio_auth_token"]
    ping_date = PingData.from_json(ping).exact_time
    client = Client(account_sid, auth_token)
    print("Sending to twillio")
    message = client.messages.create(
        to="+15005550006",
        from_="+15005550006",
        body=f"Last successful ping was sent on {ping_date}",
    )


@cache
def get_secret() -> dict:
    client = boto3.client(
        service_name="secretsmanager",
    )

    get_secret_value_response = client.get_secret_value(
        SecretId=os.environ.get(TWILLIO_SECRET_MANAGER_KEY_ENV)
    )
    return json.loads(get_secret_value_response["SecretString"])
