#!/usr/bin/python3

import sys, getopt, pprint
from player_api import PlayerApi
from config import Config
from env import Env

# Doc https://github.com/engenex/xtream-codes-api-v2/blob/main/%5BHow-To%5D%20Player%20API%20v2%20-%20Tutorials%20-%20Xtream%20Codes.pdf

if __name__ == '__main__':

    # Initiate the environment (mostly constants)
    env = Env()

    # Process command line arguments
    argList = sys.argv[1:]
    options = "c:"
    long_options = ["remote", "local"]

    arguments, values = getopt.getopt(argList, options, long_options)

    for currentArgument, currentValue in arguments:
        if currentArgument in ("-c"):
            print (("Loading config (%s)") % (currentValue))
            name = currentValue
        if currentArgument in ("--local"):
            print('Mode local')
            env.mode = 0
        if currentArgument in ("--remote"):
            print('Mode remote')
            env.mode = 1

    # Read in the configuration file
    config = Config()
    try:
        conf = config.read(name)
        provider = conf['provider']
    except FileNotFoundError:
        print('File ' + name + ' not found')
        sys.exit(0)

    # Initiate the Xtream API, pass in environment and configuration
    api = PlayerApi(env, provider)

    # Authenticate and save result into file
    auth = api.authenticate(provider)
    pprint.pp(auth)
    user = auth['user_info']

    # Only get more info if user is authenticated and active
    if user['auth'] == 1 and user['status'] == 'Active':

        # Get live categories and save into file
        live_categories = api.get_live_categories()
        #pprint.pp(live_categories)
        for category in range(2):
            pprint.pp(live_categories[category])

        # Get live streams and save into file
        live_streams = api.get_live_streams()
        #pprint.pp(live_streams)
        for stream in range(2):
            pprint.pp(live_streams[stream])

    sys.exit(0)
