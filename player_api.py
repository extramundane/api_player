#!/usr/bin/python3

import http.client

class PlayerApi:
    servername = ''
    username = ''
    password = ''
    
    def build_url(self, action):
        url = '/player_api.php?username=' + self.username +\
        '&password=' + self.password
        
        if action == 'auth':
            return url
        elif action == 'live_categories':
            url += '&action=get_live_categories'
        elif action == 'live_streams':
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
        #print(url)
        conn.request("GET", url, headers={"Host": host})
        response = conn.getresponse()
        body = response.read().decode('utf-8')
        if filename != None:
            with open(filename, "w") as f:
                f.write((str)(body))
        print(response.status, response.reason)

        
    def authenticate(self, server, user, password):
        self.servername = server
        self.username = user
        self.password = password
        
        url = self.build_url('auth')
        
        self.request(url, 'auth.json')
        
        
    def get_live_categories(self):
        url = self.build_url('live_categories')
        
        self.request(url, 'live_categories.json')
        
        
    def get_live_streams(self):
        url = self.build_url('live_streams')
        
        self.request(url, 'live_streams.json')
        
