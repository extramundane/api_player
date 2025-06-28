#!/usr/bin/python3

import sys, getopt, pprint
from player_api import PlayerApi
from config import Config
from env import Env
from category_list import CatList

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
    if auth == None:
        print("Authentication failure")
        sys.exit(0)


    user = auth['user_info']

    # Only get more info if user is authenticated and active
    if user['auth'] == 1 and user['status'] == 'Active':

        # Get live categories and save into file
        live_categories = api.get_live_categories()

        # Get live streams and save into file
        live_streams = api.get_live_streams()

        list = CatList()
        table = list.connect_live_streams(live_categories,\
            live_streams)

        # Iterate over the just created list, first entry for every
        # category sub list is the category name, all subsequent
        # entries are live stream objects
        for key in table:
            cat_id = key
            stream_list = table[key]

            n = len(stream_list)
            for index in range(n):
                entry = stream_list[index]
                if index == 0:
                    # Print category name
                    print(entry)
                else:
                    # Print stream name
                    print('   ' + entry['name'])
    else:
        print("User %s not authenticated" % (provider['username']))

    sys.exit(0)
