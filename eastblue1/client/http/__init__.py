import base64
import json
import math
import time
import traceback

import allure
import curlify
import requests
from Crypto.Cipher import AES
from requests_toolbelt.utils import dump

from constant import environment
from main import encryption


class HTTPClient(object):
    def __init__(self):

        self.path=''
        self.method = ''
        self.params = {}
        self.data = {}
        self.host=''
        self.cookies=''
        self.environment=environment
        self.headers ={}



    def get_cookie(self):
        if self.environment =='test':
            self.url = 'http://test-eastblue.xinyoudi.com/web-api/home/login'
            self.username='admin'
            self.password='mc111111'
        if self.environment =='pre':
            self.url = 'http://pre-eastblue.xinyoudi.com/web-api/home/login'
            self.username = 'luxixi'
            self.password = 'bm8fl5c1iyrszg630eha'
        if self.environment =='online':
            self.url = 'http://pre-eastblue.xinyoudi.com/web-api/home/login'
            self.username = 'luxixi'
            self.password = 'bm8fl5c1iyrszg630eha'

        text = json.dumps({
            'password': self.password,
            'time': int(time.time())
        })

        body={
            "sys_lang":"",
            "username":self.username,
            "password":encryption(text)
        }
        name = "login"
        #print(f"\n------{name}----------")
        resp = None
        try:
            resp = requests.post(url=self.url,data=body, timeout=600)
            detail = dump.dump_all(resp).decode("utf-8")
            curl = curlify.to_curl(resp.request, compressed=True)
            detail = curl + "\n\n" + detail
            #print(detail)
            allure.attach(body=detail, name=name, attachment_type=allure.attachment_type.TEXT)
        except Exception:
            detail = traceback.format_exc()
            #print(detail)
            allure.attach(body=detail, name=name, attachment_type=allure.attachment_type.TEXT)
        return resp.headers.get("Set-Cookie") if resp else None


    def send_request(self,method,path,params=None,data=None):
        self.method=method
        self.params=params
        self.data=data
        self.path=path


        if self.environment =='test':
            self.host='http://test-eastblue.xinyoudi.com'
        if self.environment =='pre':
            self.host = 'http://pre-eastblue.xinyoudi.com'
        if self.environment =='online':
            self.host = 'http://pre-eastblue.xinyoudi.com'

        self.headers = {
            # "Content-Type": "application/json",
            "cookie": self.get_cookie()
        }

        self.url = self.host + self.path
        resp={}

        if self.method == "GET":
            resp = requests.get(
                url=self.url, params=self.params, json=self.data, headers=self.headers, timeout=600)
        if self.method == "POST":
            resp = requests.post(
                url=self.url, params=self.params, json=self.data, headers=self.headers,timeout=600)

        curl = curlify.to_curl(resp.request, compressed=True)
        detail = curl + "\n\n" + dump.dump_all(resp).decode("utf-8")
        allure.attach(body=detail, name=f"[api-path]{self.path} ",
                      attachment_type=allure.attachment_type.TEXT)

        return json.loads(resp.text)