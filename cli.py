#!/usr/bin/python3


import sys, getopt
#from cli import Cli
from config import Config
from env import Env

class Cli:
    def __init__(self, argv, env):

        # Process command line arguments
        argList = argv[1:]
        options = "c:d"
        long_options = ["remote", "local", "probe="]

        arguments, values = getopt.getopt(argList, options, long_options)

        for currentArgument, currentValue in arguments:
            if currentArgument in ("-c"):
                print (("Loading config (%s)") % (currentValue))
                env.config_name = currentValue
            if currentArgument in ("--local"):
                print('Mode local')
                env.mode = 0
            if currentArgument in ("--remote"):
                print('Mode remote')
                env.mode = 1
            if currentArgument in ("-d"):
                print('Display')
                env.display = True
            if currentArgument in ("--probe"):
                print('Probe DNS %s' % (currentValue))
                env.dns_mask = currentValue



