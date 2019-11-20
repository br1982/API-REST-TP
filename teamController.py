# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:32:52 2019

@author: Balta
"""

"""from flask_api import status"""
from flask import request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from teamService import Validate
import apiExterna
import json
"""
from urlparse import urlparse
"""
"""
db_connect = create_engine('sqlite:///C:\\Users\\Balta\\PythonTest\\API-REST-TP\\chinook.db')
"""

db_connect = create_engine('sqlite:////Users/damianwajser/git/irso/br/API-REST-TP/chinook.db')

class Teams(Resource):        
    """
    Accede a este class cuando no envía nigún recurso extra
    """

    def get(self):
        try:
            conn = db_connect.connect()  
            v = Validate()
            where = v.args_query_string(v)
            
            if where:
                query = conn.execute("SELECT * FROM t_teams WHERE " + where)
            else:
                query = conn.execute("SELECT * FROM t_teams")
            
            if query:
                result = [dict(zip(tuple (query.keys()), i)) for i in query.cursor]
                return jsonify({"equipos": result})
            else:
                return None, 204
        
        except Exception as ex:
            return {"message": "[ERROR]: No se puede determinar con detalle."}, 409

    
    def post(self):
        """
        Validado parametros de body. De query_string tambien hay que validar?
        si va campo generado guardar fecha y hora aleatoria
        validar query_string
        """
        try:
            conn = db_connect.connect()
            
            msgError = Validate.nameTeam(request.json['nombre'])
            if msgError:
                return {"message": msgError}, 400
            
            if Validate.existTeam(request.json['nombre']):
                return {"message": "Ya existe el equipo!"}, 422        
            
            #msgError = Validate.isIntTelefono(request.json['telefono'])
            msgError = Validate.telefonoTeam(request.json['telefono'])
            if msgError:
                return {"message": msgError}, 400
                
            msgError = Validate.emailTeam(request.json['email'])
            if msgError:
                return {"message": msgError}, 400
            
            insert = conn.execute("INSERT INTO t_teams values(null, '{0}', '{1}', '{2}')".format(request.json['nombre'], request.json['telefono'], request.json['email']))
    
            if insert.lastrowid:
                return {'id': insert.lastrowid}, 201
            else:
                return None, 409
        except KeyError as e:
            return {"message": "Le falta algún campo requerido! Verifique que este enviando nombre, telefono y email"}, 409
        
        except Exception as ex:
            return {"message": "[ERROR]: No se puede determinar con detalle!"}, 409

    def delete(self):
        """
        Puede ser que elimine por query_string o body(?)
        """
        
        try:
            conn = db_connect.connect()        
            v = Validate()
            conditions = v.args_query_string(v)
            
            if conditions:
                query = conn.execute("DELETE FROM t_teams WHERE " + conditions)
                
                """205?? 201?? preguntar"""
                if query.rowcount:
                    return {'rowCount': query.rowcount}, 201
                else:
                    return None, 404
            else:
                return {"message": "No hay parámetros para filtrar eliminación"}, 409
            
        except Exception as ex:
            return {"message": "[ERROR]: No se puede determinar con detalle!"}, 409

    def patch(self):
        """
        Validar que actualice parcial por el query string. Tambien por body?
        no puede modificar nombre del equipo
        validar formato de los campos a modificar
        
        validar id
        obtener el filtro (query_string)
        obtener que setear
        """
        
        conn = db_connect.connect()
        
        equipo = Validate()
        error = equipo.validar_campos(equipo)
        if error is None:
            filters = equipo.args_query_string(equipo)
            fields = equipo.patch_update()
            if fields != "":
                if filters:
                    query = conn.execute("UPDATE t_teams SET %s WHERE %s" % (fields, filters))
                else:
                    query = conn.execute("UPDATE t_teams SET %s WHERE %d" % (fields))
                
                if query:                
                    return {"message": "Se actualizaron correctamente los campos: %s" % (equipo.patch_update_list_fields())}, 201
                else:
                    return 404
            else:
                return {"message": "No hay actualizaciones que aplicar!"}, 400
            
        else:
            return error
            
        """    
        except Exception as ex:
            return {"message": "[ERROR]: No se puede determinar con detalle!"}, 409
        """
    def put(self):
        """
        Validar por query_string. Puede ser que se quiera actualizar por request json (body)?
        """
        conn = db_connect.connect()
        
        equipo = Validate()        
        allFields = equipo.put_count_fields()
        
        if allFields is not None:
            return {"message": allFields}, 401
        
        
        error = equipo.validar_campos(equipo)
        if error is None:
            filters = equipo.args_query_string(equipo)    
            fields = equipo.patch_update()
            
            if filters:
                query = conn.execute("UPDATE t_teams SET %s WHERE %s" % (fields, filters))
            else:
                return {"message": "Solicitud incompleta"}, 409
                
            if query:
                return {"message": "Se actualizaron correctamente los campos: %s" % (equipo.patch_update_list_fields())}, 201
            else:
                return 404
        else:
            return error        

class TeamById(Resource):
    """
    Accede a este class cuando se quiere acceder al recurso idteam
    """
    
    def get(self, id):
        #try:
        conn = db_connect.connect()
        v = Validate()
        conditions = v.args_query_string(v)
        if v.isIntIdTeam(id) == False:
            return {"message": "Debe ser entero el idTeam"}, 400
        
        conditions = v.args_query_string(v)
        if conditions:
            query = conn.execute("SELECT * FROM t_teams WHERE idteam =%d " % int(id) + " AND " + conditions)
        else:        
            query = conn.execute("SELECT * FROM t_teams WHERE idteam =%d " % int(id))
            
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        if result:
            return jsonify(list(result)[0])
        else:
            return {"message": "No existe el equipo buscado"}, 404
        
        #except Exception as ex:
         #   return {"message": "[ERROR]: " + ex}, 409

    
    
    def delete(self, id):
        """
        Validado query_string. Tambien se debe contemplar del body?
        """
        
        conn = db_connect.connect()
        equipo = Validate()
        error = equipo.idTeam(equipo, id)
        if error:
            return error
        
        conditions = equipo.args_query_string(equipo)
        if conditions:
            query = conn.execute("DELETE FROM t_teams WHERE idteam = %d" % int(id) + " AND " + conditions)
        else:
            query = conn.execute("DELETE FROM t_teams WHERE idteam = %d" % int(id))
        
        """205?? 201?? preguntar"""
        if query.rowcount:
            return {'rowCount': query.rowcount}, 200
        return None, 404 
        """        
        except Exception as ex:
            return {"message": "[ERROR]: No se puede determinar con detalle!"}, 409
        """

    def patch(self, id):
        """
        Validar que actualice parcial por el query string. Tambien por body?
        no puede modificar nombre del equipo
        validar formato de los campos a modificar
        """
        #try:
        conn = db_connect.connect()
        
        equipo = Validate()
        error = equipo.idTeam(equipo, id)
        if error:
            return error
        
        error = equipo.validar_campos(equipo)
        if error is None:
            filters = equipo.args_query_string(equipo)    
            fields = equipo.patch_update()
            
            if filters:
                query = conn.execute("UPDATE t_teams SET %s WHERE idteam = %d AND %s" % (fields, int(id), filters))
            else:
                query = conn.execute("UPDATE t_teams SET %s WHERE idteam = %d" % (fields, int(id)))
            
            if query:
                return {"message": "Se actualizaron correctamente los campos: %s" % (equipo.patch_update_list_fields())}, 201
            else:
                return 404
        else:
            return error
        #except KeyError as e:
         #   return 
        #except Exception as ex:
         #   return {"message": "[ERROR]: No se puede determinar con detalle!"}, 409
        
    
    
    def put(self, id):
        """
        Validar por query_string. Puede ser que se quiera actualizar por request json (body)?
        """
        conn = db_connect.connect()
        
        equipo = Validate()
        error = equipo.idTeam(equipo, id)
        if error:
            return error
        
        allFields = equipo.put_count_fields()
        if allFields is not None:
            return {"message": allFields}, 401
        
        error = equipo.validar_campos(equipo)
        if error is None:
            filters = equipo.args_query_string(equipo)    
            fields = equipo.patch_update()
            
            if filters:
                query = conn.execute("UPDATE t_teams SET %s WHERE idteam = %d AND %s" % (fields, int(id), filters))
            else:
                query = conn.execute("UPDATE t_teams SET %s WHERE idteam = %d" % (fields, int(id)))
            
            if query:
                return {"message": "Se actualizaron correctamente los campos: %s" % (equipo.patch_update_list_fields())}, 201
            else:
                return 404
        else:
            return error
     
    def getNameTeam(self, id):
        #try:
        conn = db_connect.connect()
        v = Validate()
        conditions = v.args_query_string(v)
        if v.isIntIdTeam(id) == False:
            return {"message": "Debe ser entero el idTeam"}, 400
        
        conditions = v.args_query_string(v)
        if conditions:
            query = conn.execute("SELECT * FROM t_teams WHERE idteam =%d " % int(id) + " AND " + conditions)
        else:        
            query = conn.execute("SELECT * FROM t_teams WHERE idteam =%d " % int(id))
            
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        if result:
            return result[0]['nombre']
        else:
            return None
        
        #except Exception as ex:
         #   return {"message": "[ERROR]: " + ex}, 409

        
class CoachDataByTeam(Resource):
    def get(self, id):        
        team = TeamById.getNameTeam(self, id)        
        #response = apiExterna.getCoachByTeam(request.args.get("name_team"))
        response = apiExterna.getCoachByTeam(team)
        
        if response != None:
            return response
        else:
            return None, 404   
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        