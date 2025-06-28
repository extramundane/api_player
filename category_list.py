#!/usr/bin/python3

import pprint

class CatList:

    # Use list of categories and list of streams to build a hash table
    # using cat id as a key to connect them
    def connect_live_streams(self, cats, streams):
        table = dict()
        # Iterate over all categories, create keys in hash table
        for cat in cats:
            cat_id = cat['category_id']
            if not cat_id in table:
                table[cat_id] = list()
                # First entry in every sub list is the category name
                table[cat_id].append(cat['category_name'])

        # Iterate over streams and connect (apppend) them to categories
        for stream in streams:
            cat_id = stream['category_id']
            if cat_id in table:
                table[cat_id].append(stream)
        return table

