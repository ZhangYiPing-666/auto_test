# coding=utf-8
import base64

import requests
from Crypto.Cipher import AES
from urllib.parse import unquote
import xmltodict
import json
import time


def aes_encrypt(key, text):
    """
    AES加密
    :param key: 加密KEY ,必须为16位
    :param text: 原始字符串
    :return: 加密后的字符串
    """
    # 加密秘钥要设置16位
    length = 16
    assert len(key) == length
    count = len(text.encode('utf-8'))
    # text不是16的倍数那就补足为16的倍数
    if count % length != 0:
        text += '\0' * (length - (count % length))
    # 初始化加密器
    aes = AES.new(str.encode(key), AES.MODE_ECB)
    return str(base64.b64encode(aes.encrypt(str.encode(text))), encoding='utf-8')


def aes_decrypt(key, text):
    """
    AES解密
    :param key: 解密KEY ,必须为16位
    :param text: 加密后的字符串
    :return: 解密后的字符串
    """
    text = unquote(text,encoding="utf-8")
    # 加密秘钥要设置16位
    length = 16
    assert len(key) == length
    # 初始化加密器
    aes = AES.new(str.encode(key), AES.MODE_ECB)
    text = base64.decodebytes(bytes(text, encoding='utf8'))
    text = aes.decrypt(text).rstrip(b'\0')
    # text = text[::-1].split('>', 1)[-1][::-1] + '>'
    end_mark = b'</RESPONSE>'
    text = text[:text.rindex(end_mark) + len(end_mark)]
    text = str(text.decode("utf8"))
    text_dict = type_to_json(text)
    data = text_dict.get("RESPONSE")
    return data


def write_log(file_name, data):
    data_str = "\n"
    data_str =data_str + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"
    print(data)
    data_str =data_str + "FPQQLSH： " + data.get("FPQQLSH") + "\n"
    data_str =data_str + "FP_DM： " + data.get("FP_DM") + "\n"
    data_str =data_str + "FP_HM： " + data.get("FP_HM") + "\n"
    data_str =data_str + "KPRQ： " + data.get("KPRQ") + "\n"
    data_str =data_str + "FPLXDM： " + data.get("FPLXDM") + "\n"
    if data.get("FPLXDM") == "026":
        data_str =data_str + "PDF_URL： " + data.get("PDF_URL") + "\n"
        data_str =data_str + "SP_URL： " + data.get("SP_URL") + "\n"
    if data.get("FPLXDM") != "004":
        data_str =data_str + "JYM： " + data.get("JYM") + "\n"
    data_str =data_str + "-" * 60
    with open(file_name, mode='a') as f:
        f.write(data_str)
    f.close()


def write_error_log(file_name, data):
    data_str = "\n"
    data_str = data_str + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"
    data_str = data_str + str(data) + "\n"
    data_str = data_str + "-" * 60 + "\n"
    with open(file_name, mode='a') as f:
        f.write(data_str)
    f.close()


def type_to_json(xml_str):
    json_str = xmltodict.parse(xml_str, encoding='utf-8')
    json_str = json.dumps(json_str, indent=1)
    json_dict = json.loads(json_str)
    return json_dict


# 解析返回的json获得关键key值
def jiexi_json(json_data, key):
    a = key.split(".")
    value = json_data
    for i in a:
        value = value[i]
    return value


if __name__ == '__main__':

    pass
    # """AES加解密DEMO"""
    # content = "<RESPONSE><RSCODE>0</RSCODE><RSMSG>开票成功！</RSMSG><DATA><FPQQLSH>34343434</FPQQLSH><FPLXDM>45454</FPLXDM><FP_DM>3433</FP_DM><FP_HM>54545</FP_HM><KPRQ>20171017181402</KPRQ><JYM>546rggfdg45t4g</JYM><PDF_URL>PDF 下载地址</PDF_URL><SP_URL>收票地址</SP_URL></DATA></RESPONSE>"
    # # 和开具发票时的密钥相同
    # password = "16B4FCB7B970551B"
    # encrypted_content = aes_encrypt(password, content)
    # print('AES+BASE64加密值：', encrypted_content)
    # decrypted_content = aes_decrypt(password, encrypted_content)
    # # 确认解密成功
    # assert decrypted_content == content
    # r = requests.post('http://127.0.0.1:8888/api/callback', data={"req": encrypted_content})
    # # 解密响应的数据
    # decrypted_text = aes_decrypt(password, r.text)
    # print(decrypted_text)
