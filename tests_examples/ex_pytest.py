"""
This module shows some example of pytest usage.

# https://docs.pytest.org
"""

import pytest


def func1(a, b):
    """Simple fontion for examples"""
    return a + b

### simple tests

def test_func1():
    assert func1(1, 2) == 3


def test_func1_fail():
    with pytest.raises(TypeError):
        func1(1, 'b')

### use fixture

# scope:
# * "function": the default scope, the fixture is destroyed at the end of the test.
# * "class": the fixture is destroyed during teardown of the last test in the class.
# * "module": the fixture is destroyed during teardown of the last test in the module.
# * "package": the fixture is destroyed during teardown of the last test in the package.
# * "session": the fixture is destroyed at the end of the test session.
# * callable: to get a dynamic scope

# use conftest to centralize fixture without import them !

@pytest.fixture(scope="session")
def pi():
    return 3.14

def test_func1_with_fixture(pi):
    assert func1(pi, 2) == pytest.approx(5.14)


@pytest.fixture(scope="session")
def pi2(pi):
    """fixture, in fixture"""
    return pi

def test_func1_with_fixture2(pi2):
    assert func1(pi2, 2) == pytest.approx(5.14)


# use fixture like dynamics parameters

@pytest.fixture(scope="module", params=[0, 1, 2, 3])
def int_fixture_params(request):
    return request.param

def test_fixture_param(int_fixture_params):
    assert 1


@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    return request.param


@pytest.fixture(scope="function", params=[1, 2])
def otherarg(request):
    return request.param

def test_0(otherarg):
    pass


def test_1(modarg):
    pass


def test_2(otherarg, modarg):
    pass


#### use parametrize for multiple different input cases

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (3.2, 4.2, 7.4),
        (4, 5.2, 9.2),
    ]
)
def test_func1_with_parametrize(a, b, expected):
    assert func1(a, b) == expected

@pytest.mark.parametrize(
    "a, b",
    [
        (1, 'B'),
        ('A', 4.2),
    ]
)
def test_func1_fail_with_parametrize(a, b):
    with pytest.raises(TypeError):
        func1(a, b)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        pytest.param(1, 'B', None, marks=pytest.mark.xfail(raises=TypeError)),
    ]
)
def test_func1_bad_practice(a, b, expected):
    assert func1(a, b) == expected




