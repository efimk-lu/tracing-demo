import boto3
import datetime
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

cloudwatch = boto3.resource("cloudwatch")
metric = cloudwatch.Metric("PingStatus", "Ping")


def lambda_handler(event, context):
    metric.put_data(
        MetricData=[
            {
                "MetricName": metric.name,
                "Timestamp": datetime.datetime.utcnow(),
                "Value": 1,
                "Unit": "Count",
            }
        ]
    )
