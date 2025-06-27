#!/usr/bin/python3

class Env:
    AUTH = 'auth'
    AUTH_FILE = AUTH + '.json'
    LIVE_CATEGORIES = 'live_categories'
    LIVE_CATEGORIES_FILE = LIVE_CATEGORIES + '.json'
    LIVE_CATEGORIES_FILTERED_FILE = LIVE_CATEGORIES + '_filtered.json'
    LIVE_STREAMS = 'live_streams'
    LIVE_STREAMS_FILE = LIVE_STREAMS + '.json'
    LIVE_STREAMS_FILTERED_FILE = LIVE_STREAMS + '_filtered.json'

    mode = 1  # 0 - local, 1 - remote
