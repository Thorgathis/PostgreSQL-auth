# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, abort
from helper import *

app = Flask(__name__)


@app.route('/' + appName + '/get')
def get():
    username = request.args.get('username') #get arguments
    password = request.args.get('password')

    if username is not None and password is not None:
        conn = psycopg2.connect(**config()) #connct to db
        cursor = conn.cursor() #create cursor

        cursor.execute("select * from fn_get(%s, %s);",(username, password)) #exec command

        conn.close() #close connection & cursor
        cursor.close()
    else:
        return "<h1>Error 401</h1>"

    return "<h1>Success 200</h1>"


@app.route('/' + appName + '/add')
def add():
    username = request.args.get('username') #get arguments
    password = request.args.get('password')

    if username is not None and password is not None:
        conn = psycopg2.connect(**config()) #connct to db
        cursor = conn.cursor() #create cursor

        cursor.execute("select * from fn_add(%s, %s); ",(username, password)) #exec command
        conn.commit()

        conn.close() #close connection & cursor
        cursor.close()
    else:
        return "<h1>Error 401</h1>"

    return "<h1>Success 200</h1>"


@app.route('/' + appName + '/ver')
def ver():
    conn = psycopg2.connect(**config()) #connct to db
    cursor = conn.cursor() #create cursor

    cursor.execute("SELECT version()") #exec command
    fetch_data = cursor.fetchone() #fetch result

    conn.close() #close connection & cursor
    cursor.close()

    return str(fetch_data) #return version data


if __name__ == "__main__":
    app.run(debug=True, port=32601)