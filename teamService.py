# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:38:07 2019

@author: Balta
"""
from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy import create_engine
"""
db_connect = create_engine('sqlite:///C:\\Users\\Balta\\Desktop\\PythonTest\\API-REST-TP\\chinook.db')
"""
db_connect = create_engine('sqlite:////Users/damianwajser/git/irso/br/API-REST-TP/chinook.db')

class Validate(Resource):
    conditions = None
    """
    def __init__(self, nombre, telefono, email):
        self.nameTeam(nombre)
        self.telefonoTeam(telefono)
        self.emailTeam(email)
    """
    @staticmethod
    def args_query_string(self):        
        """
        conds = " AND ".join(f"{k}='{v}'" for k, v in request.args.items())                
        """
        where = ''
        for k, v in request.args.items():
            where = " AND ".join(f"{k}='{v}'" for k, v in request.args.items())                
            """
            self.setConditions(self, k, v)        
            """
        
        if where:
            return where
        else:
            return None
        
        
    def args_json_body(self):
        """
        obtener que campos voy a modificar [PATCH, POST]
        
        """
        for k, v in request.get_json():
            fieldVal = self. validar + k(v)
            fieldsValues = ", ".join(f"{k}='{v}'" for k, v in request.get_json())                
        
        if fieldsValues != None:            
            """ se elimina el ultimo AND concatenado """    
            return fieldsValues
        else:
            return None
    
    @staticmethod
    def setConditions(self, field, value):
        """
        Valida los campos enviados y concatena en variable conditions
        """
        
        """r = self.nameTeam(value)
        if r != None:
            """
        self.conditions += field + " = '" + value + "' AND "
    
    @staticmethod
    def idTeam(self, id):
        if self.isIntIdTeam(id) == False:
            return {"message": "Debe ser entero el idTeam!"}, 400
        
        if self.existIdTeam(id) == False:
            return {"message": "No existe el equipo!"}, 404

                
    @staticmethod
    def nameTeam(nombre):
        if nombre is None:
            return "Falta el nombre. Máximo 35 caracteres"    
        else:
            if len(nombre) < 5 or len(nombre) > 35:
                return "Debe ser un nombre válido. Un mínimo de 5 y máximo de 35 caracteres"
            else:
                return None
    
    def validarnombre(name):
        
        if name is None:
            return "Falta el nombre. Máximo 35 caracteres"    
        else:
            conn = db_connect.connect()
            query = conn.execute("SELECT * FROM t_teams WHERE nombre = '" + nombre + "'")
            if query.fetchone():
                return None
            else:
                if len(name) < 5 or len(name) > 35:
                    return "Debe ser un nombre válido. Un mínimo de 5 y máximo de 35 caracteres"
                else:
                    return None
    
            
        
    def existTeam(nombre):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM t_teams WHERE nombre = '" + nombre + "'")
        if query.fetchone():
            return True
        else:    
            return False
    
    @staticmethod
    def existIdTeam(id):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM t_teams WHERE idteam = '" + id + "'")
        if query.fetchone():
            return True
        else:    
            return False

    @staticmethod
    def telefonoTeam(telefono):
        if len(telefono) < 6 or len(telefono) > 15:
            return "Debe ser un teléfono válido. Mínimo 7. Máximo 15 caracteres"
        if telefono.isdigit() == False:
            return "Debe ser un teléfono válido. Solo números"
        else:
            return None
        
    def isIntTelefono(telefono):
        if int(telefono):
            return None
        else:
            return "Debe ser entero el telefono"
    
    @staticmethod
    def emailTeam(email):
        if len(email) < 5 or len(email) > 25:
            return "Debe ser un email válido. Mínimo 5 y máximo 25 caracteres"
        else:
            return None

    @staticmethod
    def isIntIdTeam(id):
        if id.isdigit():
            return True
        else:
            return False       
    """
    @staticmethod
    def regla_de_negocio():        
        params = request.get_json()
        if params['nombre']:  
            return "[Regla de negocio]: No se puede cambiar el nombre del equipo"
        else:
            return None
    """
    
    @staticmethod
    def regla_de_negocio():        
        nombre = request.json['nombre']
        if nombre:  
            return "[Regla de negocio]: No se puede cambiar el nombre del equipo"
        else:
            return None
    
    @staticmethod
    def patch_update():        
        setear = ''
        for field in request.json:                
            setear += field + " = '" + request.json[field] + "', "
                
        
        if setear != None:            
            """ se elimina el ultimo AND concatenado """    
            return setear[0:len(setear)-2]
        else:
            return None     
        
    @staticmethod        
    def patch_update_list_fields():
        fieldss = ''
        for field in request.json:                
            fieldss += field + ", "
            
        return fieldss[0:len(fieldss)-2]
        
    @staticmethod    
    def validar_campos(self):
        for field in request.json:
            if field == 'nombre':
                res = self.regla_de_negocio()
                if res != None:
                    return {"message": res}, 403
                else:
                    res = self.validarnombre(request.json[field])
                    if res != None:
                        return {"message": res}, 400
            else:
                if field == 'telefono':
                    res = self.telefonoTeam(request.json[field])
                    if res != None:
                        return {"message": res}, 400
                else:
                    if field == 'email':
                        res = self.emailTeam(request.json[field])
                        if res != None:
                            return {"message": res}, 400

    def put_count_fields(self):
        telefono = False
        email = False
        
        for field in request.json:                
            if field == 'email':
                email = True
            
            if field == 'telefono':
                telefono = True                
            
        if telefono and email:
            return None
        else:
            return "Se deben actualizar todos los campos disponibles: email y telefono"