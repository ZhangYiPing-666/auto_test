import urllib.parse
import base64
from Crypto.Cipher import AES

# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes

s='3TcqUSlEKjBhsnNHawiw74oWbn7pCqLhrP7Pgw7DNv9sgdqJlNMm8Y2zEi46bSB04GVgysVWAovt%0AaI7nLD%2FNderKEqd1QlEAzKiuEV9ZUM5ZcB7iLD3v2YadE%2FiStq1J5jENNzbUd%2Fz6varTMU4drW6X%0A2EU%2FzGVpGFDkVAZpGJnjwCHAmgmGWTUFhCK2%2B%2FDti4m7o2NvZJUhL607RPXCsfoC3ROhMSk0ix8L%0Aat1aZMK7mXvOXbD9tD2kwgAGdCKPKkLubjUSsZ6ccNSYtqP0VzYw%2FhJvN8V8hhn7F3JFIY0aXuDS%0AlwNNmStdqdo8MBFeMeoHYoBfnoePE1wU9jB0Lk0p1XyVCfQ7PMw3mYw2PyjjD3LxDjQTbIst3zEZ%0AeZ1A%0A'
s=urllib.parse.unquote(s)
base64_encrypt = base64.b64decode(s.encode('utf-8'))


# 秘钥
key = "1ACB5A680CAB7E17"
# 初始化加密器
aes = AES.new(add_to_16(key), AES.MODE_ECB)

#执行解密密并转码返回str
decrypted_text = str(aes.decrypt(base64_encrypt),encoding='utf-8').replace('\0','')
print(decrypted_text)