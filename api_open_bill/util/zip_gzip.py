#!/usr/bin/env python
# coding=utf-8
__author__ = 'Luzhuo'
__date__ = '2017/5/21'

import gzip
import base64
from io import StringIO


# 数据流base64解密，解压, 生成pdf
def zlib_demo_aaa(pdf_data, pdf_name):
    with  open('%s.pdf'%(pdf_name), 'wb') as f_out:
        data = base64.b64decode(pdf_data)
        f_out.write(gzip.decompress(data))
        f_out.flush()


#
def gzip_compress(raw_data):
    buf = StringIO()
    f = gzip.GzipFile(mode='wb', fileobj=buf)
    try:
        f.write(raw_data)
    finally:
        f.close()
    return buf.getvalue()


def gzip_uncompress(c_data):
    buf = StringIO(c_data)
    f = gzip.GzipFile(mode='rb', fileobj=buf)
    try:
        r_data = f.read()
    finally:
        f.close()
    return r_data


def compress_file(fn_in, fn_out):
    f_in = open(fn_in, 'rb')
    f_out = gzip.open(fn_out, 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()


def uncompress_file(fn_in, fn_out):
    f_in = gzip.open(fn_in, 'rb')
    f_out = open(fn_out, 'wb')
    file_content = f_in.read()
    f_out.write(file_content)
    f_out.close()



