import logging
import os

from shifumi.game import Game, User
from shifumi.utils import screen, storage, logger_handler


def main():
    # config loggers
    current_path = os.path.dirname(__file__)
    path = os.path.join(current_path, "config/log.yaml")
    logger_handler.set_config(path)

    logger = logging.getLogger(__name__)

    # create DB
    db_path = "db.json"
    db_object = storage.DB(db_path)

    try:
        # initialise player
        name = input("Enter your name: ")
        user = User(name, db_object)
        print(f"Welcome, {name}, here is your score: {user.name}")


        # begin menu interaction
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
            logger.debug("get: %s", choice)

            if choice in ["1", "2"]:
                game = Game(user, choice)
                game.start()
            elif choice == "3":
                break
            else:
                screen.clear()
                print("Wrong choice. Read instructions carefully.")
    except KeyboardInterrupt:
        screen.clear()
        logger.info("keyboard interruption !", exc_info=True)
        print("bye bye !")


if __name__ == "__main__":
    main()
