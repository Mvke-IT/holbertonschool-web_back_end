#!/usr/bin/pyhton3
""" 2-lifo_cache """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discard = self.keys.pop()
                    del self.cache_data[discard]
                    print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)