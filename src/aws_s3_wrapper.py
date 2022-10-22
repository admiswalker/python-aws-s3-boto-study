import os
import boto3


def upload_file(dst_path, src_path):
    bucket, key = dst_path.replace("s3://", "").split("/", 1)
    key = key.rstrip('/')
    file_name = os.path.basename(src_path)
    
    s3 = boto3.client('s3')
    s3.upload_file(src_path, bucket, key+'/'+file_name)
    
    return 

