from http import client
import socket
import ssl
import os

httpsConn = client.HTTPSConnection("www.fapiao.com:53087")
sock = socket.create_connection((httpsConn.host, httpsConn.port))
print(httpsConn.host, httpsConn.port)
print(sock)
cert_file = os.path.join(os.path.abspath("../"),"fapiao.cer")
httpsConn.sock = ssl.wrap_socket(sock, ca_certs=cert_file, cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_SSLv23)

body = '{"interface": {"globalInfo": {"appId": "b36bc0bcc80aef4c585246242b10ba5e143247f5dde67b7385ffc95bcf49bca3", "interfaceId": "", "interfaceCode": "DFXJ1001", "requestCode": "DZFPQZ", "requestTime": "2018-10-30 12:36:22", "responseCode": "DS", "dataExchangeId": "DZFPQZDFXJ1001201810301236933594909"}, "returnStateInfo": {"returnCode": "", "returnMessage": ""}, "Data": {"dataDescription": {"zipCode": "0"}, "content": "eyJSRVFVRVNUX0NPTU1PTl9GUEtKIjogeyJGUFFRTFNIIjogInRlc3Q1OTI4OTkxMjc3OTExNTExIiwgIktQTFgiOiAiMCIsICJaU0ZTIjogIjAiLCAiWFNGX05TUlNCSCI6ICIxMTAxMDk1MDAzMjE2NTQiLCAiWFNGX01DIjogIueZvuaXuueUteWtkOa1i+ivlTEiLCAiWFNGX0RaREgiOiAi55SY6IKD5YWw5beeODg4ODg4ODgiLCAiWFNGX1lIWkgiOiAi55SY6IKD5YWw5bee5oub5ZWG6ZO26KGMODg4ODg4ODg4IiwgIkdNRl9NQyI6ICIx6KGM5piO57uGIiwgIkdNRl9TSkgiOiAiMTgxMjg4MDU5MjAiLCAiS1BSIjogIuWImOWnkCIsICJTS1IiOiAi5ZC05YipIiwgIkZIUiI6ICLljaLmlY8iLCAiWUZQX0RNIjogIiIsICJZRlBfSE0iOiAiIiwgIkpTSEoiOiAiMTYiLCAiSEpKRSI6ICIxNi4wMCIsICJISlNFIjogIjAiLCAiSFlMWCI6ICIwIiwgIkJZOCI6ICJkMDk2ZTJkYmRiZTI0ZjkwYTc1MTVmNDc5ZTYxMzY0MCIsICJCWTkiOiAiYWRtaW4iLCAiQ09NTU9OX0ZQS0pfWE1YWFMiOiB7IkNPTU1PTl9GUEtKX1hNWFgiOiB7IkZQSFhaIjogIjAiLCAiU1BCTSI6ICIxMDMwMTAyMDEwMTAwMDAwMDAwIiwgIllIWkNCUyI6ICIxIiwgIkxTTEJTIjogIjIiLCAiWlpTVFNHTCI6ICLkuI3lvoHnqI4iLCAiWE1NQyI6ICLkuI3lvoHnqI7nmoTlpKfnsbMiLCAiWE1TTCI6ICIxIiwgIlhNREoiOiAiMTYiLCAiWE1KRSI6ICIxNiIsICJTTCI6ICIwIiwgIlNFIjogIjAifX19fQ==", "contentKey": "/TfQ+v8NDLBJXvZJ8LGaKy2Yz836355xnDpQR4Gw3fIf4oNf61xuttG5zDj6kno7"}}}'

httpsConn.request("POST", "/fpt-dsqz/invoice", body, headers=None)
res = httpsConn.getresponse()
headers = {}
for k, v in res.getheaders():
    headers[k] = v
print( res.status, headers, res.read())
