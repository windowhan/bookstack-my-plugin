import requests
import json

class RequestManager:
    headers = None
    host = None

    def __init__(self, token):
        self.headers = {}
        self.headers["Authorization"] = "Token %s:%s" % (token.tid, token.secret)
        self.host = token.host
        pass

    def get(self, url):
        print(self.host + url)
        req = requests.get(self.host + url, headers=self.headers)
        return json.loads(req.text)

    def post(self, url, data):
        print(self.host + url)
        print(data)
        req = requests.post(self.host + url, headers=self.headers, json=data)
        return json.loads(req.text)

    def put(self, url, data):
        print(self.host + url)
        req = requests.put(self.host + url, headers=self.headers, json=data)
        return json.loads(req.text)
