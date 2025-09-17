#!/usr/bin/python3

import json
from config import Config

class JsonReader:
    config = None

    def __init__(self, config):
        self.config = config


    def read(self, filename):
        with open(filename, 'r') as file:
            # TODO Allow empty file
            data = json.load(file)
        return data


    def read_file(self, name):
        data = self.read(name)
        return data


    def read_live_categories(self):
        data = self.read(config.LIVE_CATEGORIES_FILE)
        return data


    def read_live_streams(self):
        data = self.read(configt.LIVE_STREAMS_FILE)
        return data
