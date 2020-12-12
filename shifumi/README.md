# Introduction

the goal of this mini project is to make a shufumi game.

* learn basis structure of a project (setup.py, package, module, class ...)
* learn logger
* learn POO
* learn unitest / mock
* ...

# Before installation
Don't forget to create and activate your python virtual environment

# Installation

## Python environment

### production
.. code:: bash

    $ pip install .

### Dev / Test
.. code:: bash

    $ pip install -e '.[testing]'

#### to test
.. code:: bash

    $ py.test --cov=shifumi --cov-report term-missing tests/

add -s -v for more debug info

#### pylint
.. code:: bash

    $ pylint shifumi

#### Cyclomatic Complexity
.. code:: bash

    $ xenon --max-absolute C --max-modules B --max-average A shifumi

### to launch
.. code:: bash

    $ shifumi
or 
.. code:: bash

    $ python shifumi/main.py

## Docker
.. code:: bash

    $ docker build -t Dockerfile -t python_formation/shifumi .

then 

.. code:: bash

    $ docker run -it python_formation/shifumi

### to test/dev
.. code:: bash

    $ docker-compose run {format|check-format|style|complexity|test-unit}
