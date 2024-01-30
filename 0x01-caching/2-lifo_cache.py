#!/usr/bin/env python3
"""LIFO Caching

Classes:
    LIFOCache(BaseCaching)
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Represents a LIFO caching system"""

    def put(self, key, item):
        """Inserts an item into the cache"""
        if key and item:
            if (len(self.cache_data) + 1) > BaseCaching.MAX_ITEMS:
                del_key = self.cache_data.popitem()[0]

                print("DISCARD: {}".format(del_key))

            self.cache_data[key] = item

    def get(self, key):
        """Returns the value of an item in the cache."""
        if not key or key not in self.cache_data:
            return None

        return self.cache_data[key]
