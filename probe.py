#!/usr/bin/python3

class Probe:
    def probe(self, mask):
        print('Probe "%s"' % (mask))
        self.get_format(mask)
        pass

    def get_format(self, mask):
        start = mask.find('(')
        send = mask.find(')',  start + 1)
        length = send - start
        print('Start %d End %d Length %d' % (start, send, length))
        print(mask[start+1:send])

