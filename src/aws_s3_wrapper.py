import io
import os
from urllib.parse import urlparse

import boto3


def __split_s3_path(path):
    
    o = urlparse(path)
    bucket = o.hostname
    key = o.path.lstrip('/').rstrip('/')
    
    return bucket, key

def __join_keyBase_fileName(key_base, file_name):
    key = key_base+'/'+file_name if len(key_base)>0 else file_name
    return key

def upload_file(dst_path, src_path):
    
    bucket, key_base = __split_s3_path(dst_path)
    file_name = os.path.basename(src_path)
    
    key = __join_keyBase_fileName(key_base, file_name)
    
    s3 = boto3.client('s3')
    s3.upload_file(src_path, bucket, key)
    
    return

def download_file(dst_path, src_path):
    os.makedirs(dst_path, exist_ok=True)
    
    bucket, key = __split_s3_path(src_path)
    file_name = os.path.basename(src_path)
    dst_path = dst_path.rstrip('/')
    
    s3 = boto3.client('s3')
    s3.download_file(bucket, key, dst_path+'/'+file_name)
    
    return 

def download_fileobj(fp, src_path):
    
    bucket, key = __split_s3_path(src_path)
    file_name = os.path.basename(src_path)
    
    s3 = boto3.client('s3')
    s3.download_fileobj(bucket, key, fp)
    
    return

def download_as_bin(src_path):
    
    binary = ''
    with io.BytesIO() as fp:
        download_fileobj(fp, src_path)
        binary = fp.getvalue()
        
    return binary

def download_as_str(src_path, encoding):

    binary = download_as_bin(src_path)
    
    s = str(binary, encoding=encoding, errors='replace')
    
    return s

