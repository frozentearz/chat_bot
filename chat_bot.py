#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json

while 1:
    url = "http://openapi.tuling123.com/openapi/api/v2"
    text = input("I:")
    headers = {'Content-Type': 'application/json'}
    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": text
            }
        },
        "userInfo": {
            "apiKey": "f86b8f34e8464b3a9323c10963361051",
            # "apiKey": "05ba411481c8cfa61b91124ef7389767", 备用apikey，别人的
            "userId": "382603"
        }
    }
    response = requests.post(url, data=json.dumps(data), headers=headers).json()
    print("Robot:", response.get("results")[0].get("values").get("text"))
