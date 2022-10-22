import datetime as dt
import io
import os
import pandas as pd
import numpy as np
from urllib.parse import urlparse

import src.aws_s3_wrapper as s3
import src.file as fl


def main_up():
    tmp_dir = './tmp_up'
    os.makedirs(tmp_dir, exist_ok=True)

    dt_curr_jp = dt.datetime.now(dt.timezone(dt.timedelta(hours=9)))
    s_curr_jp = dt_curr_jp.strftime('%Y%m%d_%H%M_%S')

    f_name = f'test_{s_curr_jp}.txt'
    s = ''
    fl.write(tmp_dir+'/'+f_name, s)

    src_path = tmp_dir+'/'+f_name
    #dst_path = 's3://example-2022-1022/ex_dir/'
    dst_path = 's3://example-2022-1022'
    s3.upload_file(dst_path, src_path)
    
def main_dl():
    src_path = 's3://example-2022-1022/ex_dir/test_20221022_2306_22.txt'
    dst_path = './tmp_dl/abc/'
    s3.download_file(dst_path, src_path)

#main_up()
#main_dl()


def up_csv():
    print('in main()')
    
    df_data = pd.DataFrame([[111, 'aaa', 100, 123, 987],
                            [222, 'bbb', 200, 321, 777]],
                           columns=['user_id', 'user_name', 'param_1', 'param_2', 'param_3'])
    print(df_data)
    
    save_path = 'test.csv'
    df_data.to_csv(save_path, encoding='utf_8_sig', index=False)

    s3_path = 's3://example-2022-1022'
    s3.upload_file(s3_path, save_path)

def dl_and_use_aws_s3_data_in_memory():
    
    src_path = 's3://example-2022-1022/test.csv'
    s = s3.download_as_str(src_path, encoding='utf-8')
    print(s)
    print()
    
    df_tmp = pd.read_csv(io.StringIO(s))
    print(df_tmp)

#up_csv()
#dl_and_open_csv_in_memory()
dl_and_use_aws_s3_data_in_memory()

