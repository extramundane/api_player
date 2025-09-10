#!/usr/bin/python3

from flask import Blueprint
routes = Blueprint('routes', __name__)

#from .routes import *
from .auth import *
#from .daydate import *
#from .record import *
@from .analyzer import *
