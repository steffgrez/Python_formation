FROM python:3.8-slim

RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# setup a virtual env
ENV VIRTUAL_ENV=/home/appuser/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# update pip
RUN pip install -U pip setuptools

# install requirement first for fastest build
COPY requirements requirements
RUN pip install -r requirements/base.txt

# copy source
COPY shifumi shifumi

# launch setup.py
COPY README.md .
COPY setup.py .
RUN python setup.py develop

# use setup.py entry point to launch game
CMD shifumi