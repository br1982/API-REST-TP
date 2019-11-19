# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:17:25 2019

@author: Balta
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Balta\\Desktop\\API-REST-TPv1\\chinook.db'

class Team(db.model):
    __tablename__ = 't_equipos'
    
    idequipo = db.Column(db.Integer, 
                       primary_key=True, 
                       AUTOINCREMENT)
    
    nombre = db.Column(db.String(35), 
                       unique=True, 
                       nullable=False)
    
    telefono = dbColumn(db.String(15), 
                        nullable=False)
    
    email = dbColumn(db.String(25), 
                     nullable=False)
    
    created = db.Column(db.DateTime, 
                        index=False, 
                        unique=False, 
                        nullable=False)
    