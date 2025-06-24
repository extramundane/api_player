#!/usr/bin/python3

import sys, getopt
from player_api import PlayerApi
from config import Config
from env import Env

# Doc https://github.com/engenex/xtream-codes-api-v2/blob/main/%5BHow-To%5D%20Player%20API%20v2%20-%20Tutorials%20-%20Xtream%20Codes.pdf

if __name__ == '__main__':

    argList = sys.argv[1:]
    options = "c:"

    arguments, values = getopt.getopt(argList, options)

    for currentArgument, currentValue in arguments:
        if currentArgument in ("-c"):
            print (("Loading config (%s)") %\
                (currentValue))
            name = currentValue

    config = Config()
    try:
        conf = config.read(name)
        provider = conf['provider']
    except FileNotFoundError:
        print('File ' + name + ' not found')
        sys.exit(0)

    # Initiate the environment (mostly constants)
    env = Env()

    # Initiate the Xtream API
    api = PlayerApi()

    # Authenticate and save result into file
    api.authenticate(env, provider)

    # Get live categories and save into file
    api.get_live_categories(env)

    # Get live streams and save into file
    api.get_live_streams(env)

    sys.exit(0)
