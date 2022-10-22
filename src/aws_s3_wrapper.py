import os
from urllib.parse import urlparse

import boto3


def __split_s3_path(path):
    
    o = urlparse(path)
    bucket = o.hostname
    key = o.path.lstrip('/').rstrip('/')
    
    return bucket, key

def upload_file(dst_path, src_path):
    
    bucket, key = __split_s3_path(dst_path)
    file_name = os.path.basename(src_path)
    
    s3 = boto3.client('s3')
    s3.upload_file(src_path, bucket, key+'/'+file_name)
    
    return 

def download_file(dst_path, src_path):
    os.makedirs(dst_path, exist_ok=True)
    
    bucket, key = __split_s3_path(src_path)
    file_name = os.path.basename(src_path)
    dst_path = dst_path.rstrip('/')
    
    s3 = boto3.client('s3')
    s3.download_file(bucket, key, dst_path+'/'+file_name)
    
    return 

