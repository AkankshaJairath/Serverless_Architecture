import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    # Define the S3 bucket
    bucket_name = 'arpit-image-compr-s3'  # Replace with your bucket name
    
    # Calculate the date 30 days ago from today
    days_old = 1
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_old)
    
    # List objects in the bucket
    objects = s3_client.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in objects:
        for obj in objects['Contents']:
            object_key = obj['Key']
            last_modified = obj['LastModified']
            
            # If the file is older than 30 days, delete it
            if last_modified < cutoff_date:
                s3_client.delete_object(Bucket=bucket_name, Key=object_key)
                print(f"Deleted {object_key}, last modified: {last_modified}")
            else:
                print(f"Retained {object_key}, last modified: {last_modified}")
    else:
        print("Bucket is empty or no objects found.")
    
    return {
        'statusCode': 200,
        'body': 'S3 cleanup operation completed'
    }
