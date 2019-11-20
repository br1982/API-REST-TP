# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 02:57:22 2019

@author: Balta
"""

import requests
import json
from flask import jsonify

def getCoachByTeam(team):    
    url = "https://allsportsapi.com/api/football"
    
    payload = "{}"
    headers = {
    }
    
    params = {
            "met": "Teams",
            "leagueId": 11,
            "APIkey": "d7fb79e4e93ee46ad59ac59f9d5a4e7864154e5235edf559702cf31ce27c7231"
    }
    
    response = requests.get(url, data=payload, headers=headers, params=params)
    print("debug")
    print(response.status_code)
    response_json = json.loads(response.text)
    result = response_json['result']
    
    for equipo in result:
        if equipo['team_name'] == team:
            return jsonify(equipo['coaches'])

    return None