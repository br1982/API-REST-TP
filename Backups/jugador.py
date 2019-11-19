# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:50:42 2019

@author: Balta
"""

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///C:\\Users\\Balta\\PythonTest\\API-REST-tutorial\\chinook.db')

app = Flask(__name__)

api = Api(app)

class Jugador(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM players")
        return {
        'players': [i[0] for i in query.cursor.fetchall()]}
        
    def post(self):
        conn = db_connect.connect()
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        
        query = conn.execute("INSERT INTO players values(null, '{0}', '{1}')".format(nombre, apellido))
        
        return {'201': 'Jugador guardado con éxito!'}

class JugadorData(Resource):
    def get(self, jugador_id):
        conn = db_connect.connect()
        query = conn.execute("select * from players where player_id =%d " % int(jugador_id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)



api.add_resource(Jugador, '/players')  # Route_1     
api.add_resource(JugadorData, '/players/<jugador_id>')  # Route_3


if __name__ == '__main__':
    app.run();   