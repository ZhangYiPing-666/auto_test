#!/usr/bin/env python
# coding=utf-8

import base64
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


# base64加密
def encode_base64(str_test):
    str_test = base64.encodebytes(str_test.encode(encoding="utf-8"))
    str_test = str_test.decode(encoding="utf-8")
    return str_test


# base64解密
def decode_base64(str_test):
    str_test = str_test.encode(encoding="utf-8")
    str_test = base64.decodebytes(str_test)
    str_test = str_test.decode(encoding="utf-8")
    return str_test


# md5加密
def md5_str(str1):
    hl = hashlib.md5()
    hl.update(str1.encode(encoding='utf-8'))
    str_md5 = hl.hexdigest()
    return str_md5


# 秘钥字符不够16不够16，大于16补够16倍数
def pad_key(key):
    while len(key) % 16 != 0:
        key += b' '
    return key


# 加密字符不够16不够16，大于16补够16倍数
def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    return text


# 对字符aes进行加密
def en_ase_str(key, text):
    key = key.encode(encoding="utf-8")
    text = text.encode(encoding="utf-8")
    # text = pad(text)
    # key = pad_key(key)
    # 进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
    aes = AES.new(key, AES.MODE_ECB)
    encrypted_text = aes.encrypt(text)
    encrypted_text = b2a_hex(encrypted_text).decode(encoding="utf-8")
    return encrypted_text


# 对字符进行aes加密
def de_ase_str(key,text):
    key = key.encode(encoding="utf-8")
    text = text.encode(encoding="utf-8")
    text = a2b_hex(text)
    key = pad_key(key)
    aes = AES.new(key, AES.MODE_ECB)
    decrypted_text = aes.decrypt(text)
    decrypted_text = decrypted_text.rstrip(b" ")
    return decrypted_text.decode(encoding="utf-8")
















