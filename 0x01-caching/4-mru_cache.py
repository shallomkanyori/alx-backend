#!/usr/bin/env python3
"""MRU Caching

Classes:
    MRUCache(BaseCaching)
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Represents a MRU caching system"""

    usage = {}
    age = 0

    def put(self, key, item):
        """Inserts an item into the cache"""
        if key and item:
            self.cache_data[key] = item
            self.age += 1
            self.usage[key] = self.age

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                usage_sorted = sorted(self.usage.items(),
                                      key=lambda x: x[1],
                                      reverse=True)

                # Don't delete the inserted item
                del_key = (usage_sorted[0][0] if usage_sorted[0][1] != self.age
                           else usage_sorted[1][0])

                self.cache_data.pop(del_key)
                self.usage.pop(del_key)

                print("DISCARD: {}".format(del_key))

    def get(self, key):
        """Returns the value of an item in the cache."""
        if not key or key not in self.cache_data:
            return None

        self.age += 1
        self.usage[key] = self.age

        return self.cache_data[key]
