import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
sys.path.append('test/..')
import src.aws_s3_wrapper as s3

def test___split_s3_path_case01():
    s3_path = 's3://example-2022-1022/ex_dir/example.txt'
    bucket, key = s3.__split_s3_path(s3_path)
    assert(bucket=='example-2022-1022')
    assert(key=='ex_dir/example.txt')

def test___split_s3_path_case02():
    s3_path = 's3://example-2022-1022/ex_dir/'
    bucket, key = s3.__split_s3_path(s3_path)
    assert(bucket=='example-2022-1022')
    assert(key=='ex_dir')

def test___split_s3_path_case03():
    s3_path = 's3://example-2022-1022/ex_dir'
    bucket, key = s3.__split_s3_path(s3_path)
    assert(bucket=='example-2022-1022')
    assert(key=='ex_dir')

def test___split_s3_path_case04():
    s3_path = 's3://example-2022-1022/'
    bucket, key = s3.__split_s3_path(s3_path)
    assert(bucket=='example-2022-1022')
    assert(key=='')

def test___split_s3_path_case05():
    s3_path = 's3://example-2022-1022'
    bucket, key = s3.__split_s3_path(s3_path)
    assert(bucket=='example-2022-1022')
    assert(key=='')

def test___join_keyBase_fileName_case01():
    key_base = 'dir01/dir02'
    file_name = 'example.txt'
    key = s3.__join_keyBase_fileName(key_base, file_name)
    assert(key=='dir01/dir02/example.txt')

def test___join_keyBase_fileName_case02():
    key_base = ''
    file_name = 'example.txt'
    key = s3.__join_keyBase_fileName(key_base, file_name)
    assert(key=='example.txt')

