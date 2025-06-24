#!/usr/bin/python3

import json
from const import Const

class JsonReader:
    def read(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data


    def read_live_categories(self):
        data = read(Const.LIVE_CATEGORIES_FILE)
        return data


    def read_live_streams(self):
