#!/usr/bin/python3.6

import os, importlib

from flask import Flask, request

app = Flask(__name__)

@app.route('/api/<api>', methods=['POST','GET'])
def handle(api):
    if os.path.exists(f'./routes/api/{api}.py'):
        return importlib.import_module(f'routes.api.{api}').handle(request)
    else:
        return 'API not found.'

app.run(port=5050)

