# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 01:37:00 2019

@author: Balta
"""
from flask import Flask, request
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/ejemplo')
def ejemplo():
    db_connect = create_engine('sqlite:///C:\\Users\\Balta\\Desktop\\PythonTest\\API-REST-TP\\chinook.db')

    conn = db_connect.connect()
    query = conn.execute("SELECT * FROM teams")
    return query.cursor.
    


if __name__ == '__main__':
    
    """
    host='0.0.0.0', 
    """
    app.run(port=3002);  