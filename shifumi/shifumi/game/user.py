import logging


logger = logging.getLogger(__name__)


class User:
    def __init__(self, name, db):
        self._name = name

        self._db = db

        self._data = self._db.get("name", self._name)

        logger.debug(name)
        logger.debug(self._data)

        if not self._data:
            logger.debug("user not found, create it")
            self._data = {"name": self._name, "win": 0, "loss": 0}
            self._db.insert(self._data)

    def add_win(self):
        logger.debug("add_win")
        self._data["win"] += 1
        self._db.update("name", self._name, self._data)

    def add_loss(self):
        logger.debug("add_loss")
        self._data["loss"] += 1
        self._db.update("name", self._name, self._data)

    @property
    def name(self):
        return self._data["name"]

    @property
    def score(self):
        return {"win": self._data["win"], "loss": self._data["loss"]}
