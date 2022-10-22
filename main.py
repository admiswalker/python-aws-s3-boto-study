import datetime as dt
import io
import os
import pandas as pd
import numpy as np
from urllib.parse import urlparse

import src.aws_s3_wrapper as s3
import src.file as fl


def main_up():
    tmp_dir = './tmp'
    os.makedirs(tmp_dir, exist_ok=True)

    dt_curr_jp = dt.datetime.now(dt.timezone(dt.timedelta(hours=9)))
    s_curr_jp = dt_curr_jp.strftime('%Y%m%d_%H%M_%S')

    f_name = f'test_{s_curr_jp}.txt'
    s = ''
    fl.write(tmp_dir+'/'+f_name, s)

    src_path = tmp_dir+'/'+f_name
    dst_path = 's3://example-2022-1022/ex_dir/'
    s3.upload_file(dst_path, src_path)
    
def main_dl():
    print('hello')
    
    src_path = 's3://example-2022-1022/ex_dir/test_20221022_2306_22.txt'
    dst_path = './tmp_dl/abc/'
    s3.download_file(dst_path, src_path)


#main_up()
#main_dl()

