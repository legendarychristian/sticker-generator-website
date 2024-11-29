import boto3
import numpy as np
import cv2
from ultralytics import YOLO

# Initialize S3 client
s3 = boto3.client('s3')

# List objects in the bucket
bucket_name = 'input-image-storage'
directory_prefix = 'raw-images/'

response = s3.list_objects_v2(Bucket = bucket_name, Prefix = directory_prefix)

if "Contents" in response:
    for obj in response["Contents"]:
        if obj['Key'].endswith('/'):
            continue
        print(obj['Key'])

