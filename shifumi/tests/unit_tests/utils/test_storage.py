from unittest.mock import MagicMock, patch

import pytest


from shifumi.utils.storage import DB


@pytest.fixture
@patch("shifumi.utils.storage.TinyDB")
@patch("shifumi.utils.storage.Query")
def db_object(query_mock, tiny_db_mock):
    return DB("path1")


@patch("shifumi.utils.storage.TinyDB")
@patch("shifumi.utils.storage.Query")
def test_init(query_mock, tiny_db_mock):
    return DB("path1")
    tiny_db_mock.assert_called_with("path1")
    assert db_object._db == tiny_db_mock()
    assert db_object._query == query_mock()


def test_get(db_object):
    db_object.get("key1", "value1")
    # todo: get a better test !
    db_object._db.get.assert_called_once_with(False)


def test_update(db_object):
    db_object.update("key1", "value1", "data")
    # todo: get a better test !
    db_object._db.update.assert_called_once_with("data", False)


def test_insert(db_object):
    db_object.insert("data")
    # todo: get a better test !
    db_object._db.insert.assert_called_once_with("data")


def test_delete_key(db_object):
    db_object.delete_key("key1", "value1")
    # todo: get a better test !
    db_object._db.remove.assert_called_once_with(False)
