# coding=utf-8

from flask import Flask, request
from erp.aes_util import aes_decrypt, write_log, write_error_log
import os
from util.config import Config
file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
use_yml = os.path.join(file, "huanjing", "huanjing")
password = Config(use_yml).get("use").get("key")

app = Flask(__name__)
file_path = os.path.join(os.getcwd(), "report")


@app.route('/fpt-cloudservice-callback/callback', methods=['POST'])
def api_callback():
    """
    回调地址的请求方式为http 请求的Post 请求方式
    :return:
    """
    try:
        print("-"*40)
        data = aes_decrypt(password, request.form["req"])
        print(data.get("RSCODE"), print(type(data.get("RSCODE"))))
        if data.get("RSCODE") == "0":
            Ture_file_path = os.path.join(file_path, "Ture.txt")
            write_log(Ture_file_path, data.get("DATA"))
        else:
            False_file_path = os.path.join(file_path, "False.txt")
            write_error_log(False_file_path, data)
        content = '<RESPONSE><RSCODE>0000</RSCODE><RSMSG>推送成功</RSMSG></RESPONSE>'
        print("回调成功 "+data.get("DATA").get("FPQQLSH"))
    except Exception as e:
        content = '<RESPONSE><RSCODE>9999</RSCODE><RSMSG>推送失败: %s</RSMSG></RESPONSE>' % e
        print(content)
    return content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
