#!/usr/bin/python3

import requests, json, os
from json_reader import JsonReader
from info import Info
#from env import Env

# Implements the XTREAM player_api interface to the remote server
# - Authenticating
# - Retrieving live stream categories and actual live streams
# - Retrieving VOD categories and VOD streams
# - Retrieving series categories, streams and series info

class PlayerApi:
    servername = ''
    username = ''
    password = ''
    useragent = ''
    datadir = ''
    save = True
    env = None
    provider = None

    def __init__(self, env, provider):
        self.env = env
        self.provider = provider
        print('Initializing API')
        self.servername = provider['servername']
        self.username = provider['username']
        self.password = provider['password']
        self.useragent = provider['useragent']
        self.datadir = provider['datadir']


    def build_url(self, action):
        url = 'http://' + self.servername +\
        '/player_api.php?username=' + self.username +\
        '&password=' + self.password

        if action == 'auth':
            return url
        elif action == self.env.LIVE_CATEGORIES:
            url += '&action=get_live_categories'
        elif action == self.env.LIVE_STREAMS:
            url += '&action=get_live_streams'
        elif action == 'vod_categories':
            url += '&action=get_vod_categories'
        elif action == 'vod_streams':
            url += '&action=get_vod_streams'
        elif action == 'series_categories':
            url += '&action=get_series_categories'
        elif action == 'series':
            url += '&action=get_series'
        elif action == 'series_info':
            url += '&action=get_series_info'
        return url


    def request(self, url, filename):
        host = self.servername
        response = requests.get(url,\
            headers={'Host': host, 'User-Agent': self.useragent},\
            timeout=5)
        body = response.text
        # If we have a file name and save is turned on - save
        self.write_file(filename, body, response.status_code)

        if response.status_code != 200:
            print('Request response status: ' +\
                str(response.status_code))
            if response.status_code == 513:
                print('Not authorized')
            elif response.status_code == 404:
                print('Not found')
            return None
        return json.loads(body)


    # Authenticate against either a remote server or a local file
    def authenticate(self, provider):
        if self.env.mode == 1:
            print('Requesting authentication from remote')

            url = self.build_url(self.env.AUTH)

            data = self.request(url, self.provider['auth_file'])
            Info.auth_info(data)
        else:
            local = self.get_local_file(self.datadir,\
                self.provider['auth_file'])
            print("Using local file %s" % (local))
            reader = JsonReader(None)
            data = reader.read_file(local)
        return data


    # Read the live categories from either a remote server
    # or a local file
    def get_live_categories(self):
        if self.env.mode == 1:
            print('Requesting live categories from remote')
            url = self.build_url(self.env.LIVE_CATEGORIES)

            data = self.request(url,\
                self.provider['live_categories_file'])
        else:
            local = self.get_local_file(self.datadir,\
                self.provider['live_categories_file'])
            print("Using local file %s" % (local))
            reader = JsonReader(None)
            data = reader.read_file(local)
        return data


    # Read the live streams from either a remote server
    # or a local file
    def get_live_streams(self):
        if self.env.mode == 1 :
            print('Requesting live streams from remote')
            url = self.build_url(self.env.LIVE_STREAMS)

            data = self.request(url,\
                self.provider['live_streams_file'])
        else:
            local = self.get_local_file(self.datadir,\
                self.provider['live_streams_file'])
            print("Using local file %s" % (local))
            reader = JsonReader(None)
            data = reader.read_file(local)
        return data


    # Check if the datadir exists, create it if it doesn't
    # Return the combined name of the file
    def get_datadir(self, datadir, filename):
        if not os.path.isdir(datadir):
            print('Creating data directory ' + datadir)
            os.mkdir(datadir)
        return self.get_local_file(datadir, filename)


    # Get full save filename
    def get_local_file(self, datadir, filename):
        return datadir + '/' + filename


    # Wrie file
    def write_file(self, filename, body, status):
        if filename != None and self.save:
            if status != 200:
                body = '{}'
            with open(\
                self.get_datadir(self.datadir, filename), 'w') as f:
                f.write((str)(body))
