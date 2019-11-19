# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:32:52 2019

@author: Balta
"""

"""from flask_api import status"""
from flask import request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
"""
from urlparse import urlparse
"""
"""
db_connect = create_engine('sqlite:///C:\\Users\\Balta\\PythonTest\\API-REST-TP\\chinook.db')
"""

db_connect = create_engine('sqlite:///C:\\Users\\Balta\\Desktop\\PythonTest\\API-REST-TP\\chinook.db')

class Team(Resource):
    def get(self):
        """
        Ver query_string
        """
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM teams")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        
        """
        return query.cursor.fetchall(),  '200'
        """
        
        if result:
            return result, 200
        return None, 204
        
        """
        print(request.query_string)
        return 200
        """
   
    def post(self):
        """
        validar que el equipo no exista 422
        validar len de cada campo 400
        validar texto (email y nombre equipo) y numero (telefono) 400
        si va campo generado guardar fecha y hora aleatoria
        validar query_string
        """
        conn = db_connect.connect()
        if request.json['nombre'] is '':
            return {"code": "400", "message": "Falta el nombre del equipo"}, 400
        nombre = request.json['nombre']
        """
        query = conn.execute("SELECT * FROM teams WHERE nombre = %s'" % str(nombre) % "'")
        if query:
            return {"message": "Ya existe el equipo!"}, 422
        """
        
        if request.json['telefono'] is '':
            return {"code": "400", "message": "Falta el telefono del equipo"}, 400
        phone = request.json['telefono']
        
        if request.json['email'] is '':
            return {"code": "400", "message": "Falta el email del equipo"}, 400            
        email = request.json['email']
        
        direccion = 'prueba'
        cuit = 'prueba'
        
        insert = conn.execute("INSERT INTO teams values(null, '{0}', '{1}', '{2}', '{3}', '{4}')".format(nombre, cuit, direccion, email, phone))
        """
        agregar objeto que inserto
        """
        if insert.lastrowid:
            return {'id': insert.lastrowid}, 201
        else:
            return 409
        
class TeamById(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM teams WHERE idteam =%d " % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        if result:
            """
            return jsonify(result), 200
            """
            return result, 200
        return {"404": "No existe el equipo buscado"}, 404
    
    def delete(self, id):
        """
        
        """
        conn = db_connect.connect()
        query = conn.execute("DELETE FROM teams WHERE idteam = %d" % int(id))
        if query:
            return {'201': 'Se eliminó con éxito el equipo'}, 201
        return None, 404

    def patch(self, id):
        """
        no puede modificar nombre del equipo
        validar formato de los campos a modificar
        """
        setear = ''
        for field in request.json:
            setear += field + " = '" + request.json[field] + "' AND "
            
        conn = db_connect.connect()
        query = conn.execute("UPDATE teams SET %s WHERE idteam = %d" % (setear[0:len(setear)-4], int(id)))
            
        if query is '':
            return 404
        return {'201': 'Se actualizaron correctamente los campos'}, 201