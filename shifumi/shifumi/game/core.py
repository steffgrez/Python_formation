import logging
import random
import time

from shifumi.game import version1, version2
from shifumi.utils import screen


logger = logging.getLogger(__name__)


class InputException(Exception):
    pass


class ExitException(Exception):
    pass


class Game:
    def __init__(self, name, version):
        self.name = name

        if version == "1":
            self.rules = version1.rules
        elif version == "2":
            self.rules = version2.rules
        else:
            print("Unknow version game: " + str(version))
            return

    def start(self):
        screen.clear()
        logger.debug("start game")
        print(self.rules["instructions"])

        while True:
            try:
                result = self.process_turn()
            except ExitException:
                screen.clear()
                break
            except InputException:
                screen.clear()
                print()
                print("Wrong Input!!")
                continue

    def process_turn(self):
        logger.debug("process turn")
        result = self.input_player_move()

        if result.lower() == "help":
            screen.clear()
            print(self.rules["instructions"])
        elif result.lower() == "exit":
            raise ExitException()
        elif result.isdigit() and int(result) in self.rules["game_map"]:
            self.resolve_turn(int(result))
            print("=" * 50)
            time.sleep(2)
        else:
            raise InputException()

    def input_player_move(self):
        logger.debug("input player move")
        print(
            """
--------------------------------------
                Menu
--------------------------------------
Enter "help" for instructions
Enter a number to play: 
{}
Enter "exit" to quit
--------------------------------------
        """.format(
                "\n".join(
                    [
                        "\t{}. {}".format(key, value)
                        for key, value in self.rules["game_map"].items()
                    ]
                )
            )
        )

        print()

        # Player Input
        result = input("Enter your move : ")
        logger.debug("get value:" + result)

        return result

    def resolve_turn(self, player_move):
        logger.debug("resolve turn with ia")
        print("Computer making a move....")
        time.sleep(1)

        # Get the computer move randomly
        comp_move = random.randint(0, 2)
        print("Computer chooses ", self.rules["game_map"][comp_move].upper())

        # Find the winner of the match
        winner = self.rules["winner"][player_move][comp_move]

        # Declare the winner
        if winner == player_move:
            print(self.name, "WINS!!!")
        elif winner == comp_move:
            print("COMPUTER WINS!!!")
        else:
            print("TIE GAME")
