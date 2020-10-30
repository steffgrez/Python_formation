from logging.config import dictConfig

import yaml


def set_config(path):
    # logger configuration
    with open(path, "r") as stream:
        try:
            log_config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    dictConfig(log_config)
