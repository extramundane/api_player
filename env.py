#!/usr/bin/python3

class Env:
    VERSION = '0.1.0'
    AUTH = 'auth'
    AUTH_FILE = AUTH + '.json'
    LIVE_CATEGORIES = 'live_categories'
    LIVE_CATEGORIES_FILE = LIVE_CATEGORIES + '.json'
    LIVE_CATEGORIES_FILTERED_FILE = LIVE_CATEGORIES + '_filtered.json'
    LIVE_STREAMS = 'live_streams'
    LIVE_STREAMS_FILE = LIVE_STREAMS + '.json'
    LIVE_STREAMS_FILTERED_FILE = LIVE_STREAMS + '_filtered.json'
    DATA_DIR = 'data/'

    mode = 1  # 0 - local, 1 - remote
    config_name = ''

    category_white_list = list()

    def has_white_list(self):
        return len(self.category_white_list) > 0


    def get_white_list(self):
        return self.category_white_list
