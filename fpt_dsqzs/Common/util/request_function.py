#!/usr/bin/env python
# coding=utf-8
"""封装常用请求接口函数"""
import requests
import suds
from suds.client import Client


def req_post(req_dict):
    method = req_dict.get("method")
    url = req_dict.get("url")
    headers = req_dict.get("headers")
    data = req_dict.get("data")
    params = req_dict.get("params")
    cookies = req_dict.get("cookies")
    response = requests.request(method=method, url=url, headers=headers, data=data, params=params, verify=False, cookies=cookies).text
    return response


def req_get(req_dict):
    method = req_dict.get("method")
    url = req_dict.get("url")
    headers = req_dict.get("headers")
    data = req_dict.get("data")
    params = req_dict.get("params")
    cookies = req_dict.get("cookies")
    response = requests.request(method=method, url=url, headers=headers, data=data, params=params, verify=False, cookies=cookies).text
    return response


def req_webservice(req_dict):
    client = suds.client.Client(req_dict.get("url"))
    response = client.service.getHealthyHeBei("")
    return response


def req(req_dict):
    response = ""

    if req_dict.get("method") == "GET":
        response = req_get(req_dict)

    if req_dict.get("method") == "POST":
        response = req_post(req_dict)

    if req_dict.get("method") == "POST":
        response = req_webservice(req_dict)

    return response
