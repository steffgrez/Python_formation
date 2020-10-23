import logging
from logging.config import dictConfig
import os

import yaml

from shifumi.game import Game
from shifumi.utils import screen

# logger configuration
current_path = os.path.dirname(__file__)
with open(os.path.join(current_path, "config/log.yaml"), "r") as stream:
    try:
        log_config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
dictConfig(log_config)


logger = logging.getLogger(__name__)


def main():
    name = input("Enter your name: ")

    while True:

        print(
            """
        Let's Play!!!
        Which version of Rock-Paper-Scissors?
        Enter 1 to play Rock-Paper-Scissors
        Enter 2 to play Rock-Paper-Scissors-Lizard-Spock
        Enter 3 to quit
        """
        )

        choice = input("Enter your choice = ")
        logger.debug("get:" + choice)

        if choice in ["1", "2"]:
            game = Game(name, choice)
            game.start()
        elif choice == "3":
            break
        else:
            screen.clear()
            print("Wrong choice. Read instructions carefully.")


if __name__ == "__main__":
    main()
