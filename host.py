import boto3

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

# # Download a file
# s3.download_file(bucket_name, "your-file-name", "local-file-name")

# # Upload a file
# s3.upload_file("local-file-name", bucket_name, "your-file-name")
