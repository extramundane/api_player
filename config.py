#!/usr/bin/python3

import json

class Config:
    def read(self, name):
        with open(name) as f:
            d = json.load(f)
            print(d)
            return d

            
