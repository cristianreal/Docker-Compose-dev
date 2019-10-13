from typing import List, Dict
from flask import Flask, redirect,url_for, request
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def index():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'testdb'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(buffered=True)
    cursor.execute('SELECT * FROM Clientes')
    resultado = str(cursor.fetchall())
    cursor.close()
    connection.close()
    return resultado


@app.route('/nuevoCliente')
def nuevoCliente():
    print(request)
    nombre = request.args['nombre']
    email = request.args['correo']
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'testdb'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(buffered=True)
    cursor.execute('INSERT INTO Clientes (nombre, email) VALUES (\''+nombre+'\', \''+email+'\')')
    connection.commit()
    connection.close()
    return "Guardado Nombre ["+nombre+"] correo ["+email+"]"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="80")