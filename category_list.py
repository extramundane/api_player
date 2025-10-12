#!/usr/bin/python3

import pprint
from env import Env

class CatList:
    table = dict()
    env = None

    def __init__(self, cats, env):
        self.env = env
        self.build_category_table(cats)


    def build_category_table(self, cats):
        for cat in cats:
            cat_id = cat['category_id']
            if not cat_id in self.table:
                # self.table[cat_id] = list()
                # First entry in every sub list is the category name
                self.table[cat_id] = cat['category_name']
    

    def check_whitelist(self):
        #print('White list : ' + str(self.env.category_white_list))
        count = dict()
        result = list()
        for id in self.table:
            name = self.table[id]
            for prefix in self.env.category_white_list:
                # print(name, prefix)
                if name.startswith(prefix):
                    result.append(name)
                    if self.env.display:
                        print('  ' + name)
                    if prefix in result:
                        count[prefix] += 1
                    else:
                        count[prefix] = 1
        # pprint.pprint(result)
        # pprint.pprint(count)
        return result, count


    # Use list of categories and list of streams to build a hash table
    # using cat id as a key to connect them
    def connect_live_streams(self, cats, streams):
        table = self.build_category_table(cats)

        # Iterate over streams and connect (apppend) them to categories
        for stream in streams:
            cat_id = stream['category_id']
            if cat_id in table:
                table[cat_id].append(stream)
        return table

