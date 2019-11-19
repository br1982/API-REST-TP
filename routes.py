# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:54:40 2019

@author: Balta
"""
from teamController import Teams, TeamById, CoachDataByTeam
from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app, resources={r"/teams/*": {"origins": "*"}})


api = Api(app)        


api.add_resource(Teams, '/teams')  # Route_1     
api.add_resource(TeamById, '/teams/<id>')  # Route_2"""
api.add_resource(CoachDataByTeam, '/teams/<id>/coaches') #Route_3
#api.add_resource(CoachDataByTeam, '/teams/<id>/players') #Route_3


if __name__ == '__main__':    
    
    app.run(host='0.0.0.0', port=3002);   
    

#https://allsportsapi.com/soccer-api-documentation
    