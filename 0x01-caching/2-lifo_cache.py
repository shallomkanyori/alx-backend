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
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                keys = list(self.cache_data.keys())
                del_key = keys[-2]
                self.cache_data.pop(del_key)

                print("DISCARD: {}".format(del_key))

    def get(self, key):
        """Returns the value of an item in the cache."""
        if not key or key not in self.cache_data:
            return None

        return self.cache_data[key]
