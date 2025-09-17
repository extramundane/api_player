#!/usr/bin/python3

from datetime import datetime

class Info:
    @staticmethod
    def auth_info(auth):
        user_keys = ['username', 'password', 'message', 'auth',\
            'status', 'exp_date']
        server_keys = ['url', 'port', 'timezone']
        if auth != None:
            if 'user_info' in auth:
                print('\nUser')
                user = auth['user_info']
                for key in user_keys:
                    if str(key) == 'exp_date':
                        date_object = datetime.fromtimestamp(\
                            int(user[key]))
                        print('  ' + str(key) + ' : ' +\
                            str(date_object.date()))
                    else:
                        print('  ' + str(key) + ' : ' + str(user[key]))
            if 'server_info' in auth:
                print('\nServer')
                server = auth['server_info']
                for key in server_keys:
                    print('  ' + str(key) + ' : ' + str(server[key]))
