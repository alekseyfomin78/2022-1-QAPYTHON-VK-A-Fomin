#!/usr/bin/env python3.10

import json
import os
import threading

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

SURNAME_DATA = {}


@app.route('/create_surname/', methods=['POST'])
def create_user_surname():
    name = json.loads(request.data)['name']
    surname = json.loads(request.data)['surname']
    if name not in SURNAME_DATA:
        SURNAME_DATA[name] = surname
        data = {name: surname}
        return jsonify(data), 201
    else:
        return jsonify(f'User surname {name} already exists'), 400


@app.route('/get_surname/<name>/', methods=['GET'])
def get_user_surname(name: str):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user {name} not found'), 404


@app.route('/update_surname/<name>/', methods=['PUT'])
def update_user_surname(name: str):
    surname = json.loads(request.data)['surname']
    if name in SURNAME_DATA:
        SURNAME_DATA[name] = surname
        data = {name: surname}
        return jsonify(data), 201
    else:
        return jsonify(f'User {name} and his surname {surname} are not exists'), 400


@app.route('/delete_surname/<name>/', methods=['DELETE'])
def delete_user_surname(name: str):
    if name in SURNAME_DATA:
        surname = SURNAME_DATA.pop(name)
        data = {name: surname}
        return jsonify(data), 204
    else:
        return jsonify(f'User {name} is not exist'), 400


# use case 1
# if __name__ == '__main__':
#     host = os.environ.get('MOCK_HOST', '127.0.0.1')
#     port = os.environ.get('MOCK_PORT', '4444')
#
#     app.run(host, port)

# use case 2
# запуск сервера на отдельном потоке
def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


# use case 2
def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.mock_server.shutdown')
    if terminate_func:
        terminate_func()


# use case 2
@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200
