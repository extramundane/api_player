#!/usr/bin/python3

import http.client, json
from json_reader import JsonReader
#from env import Env

class PlayerApi:
    servername = ''
    username = ''
    password = ''
    save = True
    env = None
    provider = None

    def __init__(self, env, provider):
        self.env = env
        self.provider = provider
        print('Initializing API')


    def build_url(self, action):
        url = '/player_api.php?username=' + self.username +\
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
        conn = http.client.HTTPConnection(host)

        conn.request("GET", url, headers={"Host": host})
        response = conn.getresponse()
        body = response.read().decode('utf-8')
        if filename != None and self.save:
            with open(filename, "w") as f:
                f.write((str)(body))
        print(response.status, response.reason)

        return json.loads(body)


    def authenticate(self, provider):
        if self.env.mode == 1:
            print('Requesting authentication from remote')
            self.servername = provider['servername']
            self.username = provider['username']
            self.password = provider['password']

            url = self.build_url(self.env.AUTH)

            data = self.request(url, self.provider['auth_file'])
        else:
            print("Using local file %s" %\
                (self.provider['auth_file']))
            reader = JsonReader(None)
            data = reader.read_file(\
                self.provider['auth_file'])
        return data


    def get_live_categories(self):
        if self.env.mode == 1:
            print('Requesting live categories from remote')
            url = self.build_url(self.env.LIVE_CATEGORIES)

            data = self.request(url,\
                self.provider['live_categories_file'])
        else:
            print("Using local file %s" %\
                (self.provider['live_categories_file']))
            reader = JsonReader(None)
            data = reader.read_file(\
                self.provider['live_categories_file'])
        return data


    def get_live_streams(self):
        if self.env.mode == 1 :
            print('Requesting live streams from remote')
            url = self.build_url(self.env.LIVE_STREAMS)

            data = self.request(url,\
                self.provider['live_streams_file'])
        else:
            print("Using local file %s" %\
                (self.provider['live_streams_file']))
            reader = JsonReader(None)
            data = reader.read_file(\
                self.provider['live_streams_file'])
        return data
