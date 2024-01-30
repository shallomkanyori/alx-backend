#!/usr/bin/env python3
"""LFU Caching

Classes:
    LFUCache(BaseCaching)
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Represents a LFU caching system"""

    freq = {}
    usage = {}
    age = 0

    def put(self, key, item):
        """Inserts an item into the cache"""
        if key and item:
            self.cache_data[key] = item

            self.age += 1
            self.usage[key] = self.age
            self.freq[key] = self.freq.get(key, 0) + 1

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # sort by frequency then usage
                freq_sorted = sorted(self.freq.items(),
                                     key=lambda x: (x[1], self.usage[x[0]]))

                del_key = (freq_sorted[0][0]
                           if self.usage[freq_sorted[0][0]] != self.age
                           else freq_sorted[1][0])

                self.cache_data.pop(del_key)
                self.usage.pop(del_key)
                self.freq.pop(del_key)

                print("DISCARD: {}".format(del_key))

    def get(self, key):
        """Returns the value of an item in the cache."""
        if not key or key not in self.cache_data:
            return None

        self.age += 1
        self.usage[key] = self.age
        self.freq[key] += 1

        return self.cache_data[key]
