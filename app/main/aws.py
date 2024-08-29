import os
import boto3
from config import Config

s3_client = boto3.client(
    "s3",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_ACCESS_SECRET_ID,
    region_name=Config.AWS_REGION,
)

BUCKET_NAME = Config.AWS_BUCKET_NAME
