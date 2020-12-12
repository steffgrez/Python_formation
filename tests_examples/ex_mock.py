from unittest import mock

import asynctest
import pytest

# test simple

def func1(a, b):
    return a + b


def test_func1():
    assert func1(1, 2) == 3


def test_func1_fail():
    with pytest.raises(TypeError):
        func1(1, 'b')


# use parametrize for multiple different input cases
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (3.2, 4.2, 7.4),
    ]
)
def test_func1_bis(a, b, expected):
    assert func1(a, b) == expected

# use parametrize for multiple different input cases
@pytest.mark.parametrize(
    "a, b",
    [
        (1, 'B'),
        ('A', 4.2),
    ]
)
def test_func1_fail_bis(a, b):
    with pytest.raises(TypeError):
        func1(a, b)

# use parametrize for multiple different input cases

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        pytest.param(1, 'B', None, marks=pytest.mark.xfail(raises=TypeError)),
    ]
)
def test_func1_bad_practice(a, b, expected):
    assert func1(a, b) == expected


#############
# simple mock

import random


def func2(a):
    dice_result = random.randint(1, 100)
    if a > dice_result:
        return "loose"
    else:
        return "win"


@mock.patch('random.randint', return_value=90)
def test_func2(rnd_mock):
    assert func2(5) == 'win'
    assert func2(89) == 'win'
    assert func2(91) == 'loose'
    assert rnd_mock.call_count == 3


@pytest.mark.parametrize(
    "a, random_value, expected",
    [
        (5, 90, "win"),
        (91, 90, "loose"),
    ]
)
@mock.patch('random.randint', return_value=90)
def test_func2_bis(a, random_value, expected, rnd_mock):
    assert func2(a) == expected
    assert rnd_mock.call_count == 1


@pytest.mark.parametrize(
    "a, random_value, expected",
    [
        (5, 90, "win"),
        (91, 90, "loose"),
        (5, 10, "win"),
        (91, 10, "loose"),
    ]
)
def test_func2_bis(a, random_value, expected):
    with mock.patch('random.randint', return_value=random_value) as rnd:
        assert func2(a) == expected
        assert rnd.call_count == 1

    # or without context (in case for example lot of nested patch or you want
    # use in the setUp/tearDown)
    mocker = mock.patch('random.randint', return_value=random_value)
    rnd = mocker.start()
    assert func2(a) == expected
    assert rnd.call_count == 1
    rnd.assert_called_with(1, 100)
    mocker.stop()

    # you can also use the python decorator @mock.patch() if you havn't a
    # parametrize decorator.


# more complex example with asyncio
# need asynctest and pytest-asyncio

class Database():
    async def get(self, key):
        # get value with await
        pass

    async def set(self, key, value):
        # set value with await
        pass


class Obj1():
    def __init__(self, database):
        self._database = database

    async def set_something(self, key, a, b):
        result = a + b
        try:
            await self._database.set(key, result)
            return True
        except Exception:
            return False

    async def get_something(self, key):
        return await self._database.get(key)


@pytest.fixture
def database():
    database = asynctest.mock.Mock(spec=Database)
    database.get.side_effect = [2, 3]

    return database


@pytest.mark.asyncio
async def test_obj1_set_something(database):
    obj1 = Obj1(database)

    assert await obj1.set_something('a', 2, 4) is True
    assert database.mock_calls == [
        mock.call.set('a', 6)
    ]


@pytest.mark.asyncio
async def test_obj1_get_something(database):
    obj1 = Obj1(database)

    assert await obj1.get_something('toto') == 2
    assert await obj1.get_something('titi') == 3
    assert database.mock_calls == [
        mock.call.get('toto'),
        mock.call.get('titi'),
    ]


@pytest.fixture
def database_exception():
    database = asynctest.Mock()
    database.set = asynctest.Mock(side_effect=Exception)
    database.get = asynctest.Mock(side_effect=Exception)

    return database


@pytest.mark.asyncio
async def test_obj1_set_something_fail(database_exception):
    obj1 = Obj1(database)

    with pytest.raises(Exception):
        assert await obj1.set_something('a', 2, 4) is True


@pytest.mark.asyncio
async def test_obj1_get_something_fail(database_exception):
    obj1 = Obj1(database)

    with pytest.raises(Exception):
        assert await obj1.get_something('toto') == 2
