# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 01:15:50 2019

@author: Balta
"""

import requests

if __name__ == '__main__':
    url = "https://myapptaller6.herokuapp.com/players/5dcc257c9620d41f5caf0464"
    #url = "https://google.com.ar"
    url ="https://allsportsapi.com/api/football/?met=Leagues&APIkey=d7fb79e4e93ee46ad59ac59f9d5a4e7864154e5235edf559702cf31ce27c7231&countryId=41"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print(response.content)
    else:
        print(response)
        
        