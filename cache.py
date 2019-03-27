# import datetime time library to
# use as default controller.
import datetime


class Cache:
    """
        Default class signature.
    """

    def __init__(self):
        """
            Default class constructor.
        """
        self.cache = {}
        self.MaxSize = 5

    def empty(self):
        """
            Cleaning the cache.

            :return:
        """
        return self.cache == {}

    def size(self):
        """
            Return the size of the cache.

            :return:
        """
        return len(self.cache)

    def __contains__(self, key):
        """
            Returns Boolean value, whether key is in the cache

            :param key:
            :return:
        """
        return key in self.cache

    def view(self):
        """
            Returns cache dictionary

            :return:
        """
        return self.cache

    def update(self, key, value):
        """
            Update cache and remove oldest item, when size reaches maximum

            :param key:
            :param value:
            :return:
        """
        if key not in self.cache and len(self.cache) >= self.MaxSize:
            self.delete()

        self.cache[key] = {'Added time': datetime.datetime.now().isoformat(),
                           'value': value}

    def delete(self):
        """
            Remove oldest item from cache

            :return:
        """
        old_entry = None
        for key in self.cache:
            if old_entry is None:
                old_entry = key
            elif self.cache[key]['Added time'] < self.cache[old_entry]['Added time']:
                old_entry = key
        self.cache.pop(old_entry)
