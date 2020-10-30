import logging

from tinydb import TinyDB, Query


logger = logging.getLogger(__name__)


class DB:
    def __init__(self, path):
        self._db = TinyDB(path)
        self._query = Query()

    def get(self, key, value):
        logger.debug("%s -> %s", key, value)
        return self._db.get(self._query[key] == value)

    def update(self, key, value, data):
        logger.debug("%s -> %s: %s", key, value, data)
        self._db.update(data, self._query[key] == value)

    def insert(self, data):
        self._db.insert(data)

    def delete_key(self, key, value):
        self._db.remove(self._query[key] == value)
