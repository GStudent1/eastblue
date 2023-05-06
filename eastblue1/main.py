# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import base64
import json
import math
import time

import execjs
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA


def read_public_key(file_path="crypto_public_key.pem") -> bytes:
    with open(file_path, "rb") as x:
        b = x.read()
        return b


def encryption(text: str):
    # 字符串指定编码（转为bytes）
    public_key = read_public_key()
    text = text.encode('utf-8')
    # 构建公钥对象
    cipher_public = PKCS1_v1_5.new(RSA.importKey(public_key))
    # 加密（bytes）
    text_encrypted = cipher_public.encrypt(text)
    # base64编码，并转为字符串
    text_encrypted_base64 = base64.b64encode(text_encrypted).decode()
    return text_encrypted_base64


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    text = json.dumps({
        "password": 'mc111111',
        'time': int(time.time())
    })
    print(text)
    print(type(text))
    text_encrypted_base64 = encryption(text)
    print(int(time.time()))
    print(text_encrypted_base64)

