import datetime as dt
import io
import os
import pandas as pd
import numpy as np
from urllib.parse import urlparse

import src.aws_s3_wrapper as s3
import src.file as fl


def main():
    print('hello')

    tmp_dir = './tmp'
    os.makedirs(tmp_dir, exist_ok=True)

    dt_curr_jp = dt.datetime.now(dt.timezone(dt.timedelta(hours=9)))
    s_curr_jp = dt_curr_jp.strftime('%Y%m%d_%H%M_%S')

    f_name = f'test_{s_curr_jp}.txt'
    s = ''
    fl.write(tmp_dir+'/'+f_name, s)

    src_path = tmp_dir+'/'+f_name
    dst_path = 's3://example-2022-1022/ex_dir/ex_dir2'
    s3.upload_file(dst_path, src_path)
    
def test():
    s = 's3://example-2022-1022/ex_dir/ex_dir2/abc.txt'
    #s = 's3://example-2022-1022/ex_dir/ex_dir2/'
    s = 's3://example-2022-1022/ex_dir/ex_dir2'
    
    #bucket, key = s.replace("s3://", "").split("/", 1)
    bucket, key = s.replace("s3://", "").split("/", 1)
    key = key.rstrip('/')
    print(bucket)
    print(key)

    #o = urlparse('s3://bucket_name/folder1/folder2/file1.json', allow_fragments=False)
    o = urlparse(s, allow_fragments=False)
    print(o.netloc)
    print(o.path)

    r = os.path.dirname(s)
    print(r)

main()
#test()

