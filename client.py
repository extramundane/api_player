#!/usr/bin/python3

import sys
from config import Config
from env import Env
from cli import Cli
from probe import Probe
from player_api import PlayerApi

# Doc https://github.com/engenex/xtream-codes-api-v2/blob/main/%5BHow-To%5D%20Player%20API%20v2%20-%20Tutorials%20-%20Xtream%20Codes.pdf

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


    # Initiate the Xtream API, pass in environment and configuration
    api = PlayerApi(env, provider)

    if env.dns_mask != None:
        probe = Probe()
        probe.probe(env.dns_mask)
        exit(0)

    # Authenticate and save result into file
    auth = api.authenticate(provider)
    if auth == None:
        print('Authentication failure')
        sys.exit(0)
    exit(0)
