#!/usr/bin/python3

import sys, threading, pprint
from config import Config
from env import Env
from cli import Cli
from probe import Probe
from player_api import PlayerApi
from timer import Timer
from category_list import CatList

# Doc https://github.com/engenex/xtream-codes-api-v2/blob/main/%5BHow-To%5D%20Player%20API%20v2%20-%20Tutorials%20-%20Xtream%20Codes.pdf

def isAuthenticated(auth):
    user = auth['user_info']
    return user['auth'] == 1 and user['status'] == 'Active'

def getLiveCategories():
    live_categories = api.get_live_categories()

if __name__ == '__main__':

    # Initiate the environment (mostly constants)
    env = Env()

    # Read command line options, pass command line and store in
    # environment
    cli = Cli(sys.argv, env)

    # Read in the configuration file, isolate 'provider' section
    config = Config(env)
    try:
        conf = config.read(env.config_name)
        provider = conf['provider']
    except FileNotFoundError:
        print('File "' + env.config_name + '" not found')
        sys.exit(0)

    # pprint.pprint(env.get_white_list())

    # Initiate the Xtream API, pass in environment and configuration
    api = PlayerApi(env, provider)
    timer = Timer()

    if env.dns_mask != None:
        probe = Probe()
        probe.probe(env.dns_mask)
        exit(0)

    # Authenticate and save result into file
    timer.start()
    auth = api.authenticate(provider)
    timer.stop()

    if auth == None:
        print('Authentication failure')
        sys.exit(1)

    if isAuthenticated(auth):
        print("User %s authenticated" % (auth['user_info']['username']))

        # Get live categories and save into file
        timer.start()
        live_categories = api.get_live_categories()

        list = CatList(live_categories, env)
        list.check_whitelist()

        # Get live streams and save into file
        live_streams = api.get_live_streams()
        timer.stop()
    else:
        print("User %s not authenticated" %(auth['user_info']['username']))
        exit(2)

    exit(0)
