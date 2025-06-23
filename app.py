#!/usr/bin/python3

import sys
from player_api import PlayerApi
from config import Config

if __name__ == '__main__':
    
    #args = len(sys.argv)
    argList = sys.argv[1:]
    options = "c:"
    
    for currentArgument, currentValue in argList:
        if currentArgument in ("-c"):
            print (("Enabling special output mode (% s)") %\
                (currentValue))
    
    config = Config()
    try:
        conf = config.read('config.json')
        provider = conf['provider']
    except FileNotFoundError:
        print('File ' + name + ' not found')
        sys.exit(0)
    
    api = PlayerApi()
    
    api.authenticate(\
        provider['servername'], provider['username'],\
        provider['password'])

    api.get_live_categories()
    
    api.get_live_streams()
    sys.exit(0)
