#!/usr/bin/python3

from flask import Flask
from routes import *

app = Flask(__name__)
app.register_blueprint(routes)

app.run(host="0.0.0.0", port=5000, debug=True)

