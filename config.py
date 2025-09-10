#!/usr/bin/python3

import json
from env import Env

class Config:
    env = None

    def __init__(self, environment):
        self.env = environment


    def read(self, name):
        with open(name) as f:
            d = json.load(f)
            # Do we have a white list?
            if 'category_white_list' in d['local']:
                print('Found white list entry')
                self.env.category_white_list =\
                    d['local']['category_white_list']
            return d



