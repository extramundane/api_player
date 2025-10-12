#!/usr/bin/python3

import datetime

class Timer:
    elapsed = 0

    def start(self):
        self.elapsed = datetime.datetime.now()

    def stop(self):
        self.elapsed = datetime.datetime.now() - self.elapsed
        print('Elapsed %d milliseconds' % (self.elapsed.total_seconds() * 1000))