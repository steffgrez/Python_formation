from unittest.mock import MagicMock

import pytest

from shifumi.game.user import User


def test_init_new_user():

    # test with empty db
    name = "toto"
    db_mock = MagicMock()
    db_mock.get.return_value = None
    user = User(name, db_mock)
    assert user._name == name

    result = {"name": name, "win": 0, "loss": 0}
    db_mock.insert.assert_called_with(result)
    assert user._data == result


def test_init_user():

    # test with "existing db"
    name = "toto"
    fixture = {"name": name, "win": 5, "loss": 3}
    db_mock = MagicMock()
    db_mock.get.return_value = fixture
    user = User(name, db_mock)
    assert user._name == name

    db_mock.insert.assert_not_called()
    assert user._data == fixture


def test_get_name():
    # test with "existing db"
    name = "toto"
    result = {"name": name, "win": 5, "loss": 3}
    db_mock = MagicMock()
    db_mock.get.return_value = result
    user = User(name, db_mock)

    assert user.name == name


def test_get_score():
    # test with "existing db"
    name = "toto"
    fixture = {"name": name, "win": 5, "loss": 3}
    result = {"win": 5, "loss": 3}
    db_mock = MagicMock()
    db_mock.get.return_value = fixture
    user = User(name, db_mock)

    assert user.score == result


def test_add_win():
    # test with "existing db"
    name = "toto"
    fixture = {"name": name, "win": 5, "loss": 3}
    db_mock = MagicMock()
    db_mock.get.return_value = fixture
    user = User(name, db_mock)
    user.add_win()

    assert user._data == {"name": name, "win": 6, "loss": 3}


def test_add_loss():
    # test with "existing db"
    name = "toto"
    fixture = {"name": name, "win": 5, "loss": 3}
    db_mock = MagicMock()
    db_mock.get.return_value = fixture
    user = User(name, db_mock)
    user.add_loss()

    assert user._data == {"name": name, "win": 5, "loss": 4}
