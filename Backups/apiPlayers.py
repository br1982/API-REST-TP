# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 07:17:54 2019

@author: Balta
"""

import requests

url = "https://myapptaller6.herokuapp.com/players/5dcc257c9620d41f5caf0464"
#url = "https://google.com.ar"

response = requests.request("GET", url)

print(response)