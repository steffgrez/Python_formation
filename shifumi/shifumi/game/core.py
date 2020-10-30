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

    RULES = {
        '1': version1.rules,
        '2': version2.rules,
    }

    def __init__(self, user, version):
        self._user = user

        if version in self.RULES:
            self._rules = self.RULES[version]
        else:
            logger.error("Unknow version game: " + str(version))
            raise InputException()

    def start(self):
        screen.clear()
        logger.debug("start game", stack_info=True)
        print(self._rules["instructions"])

        while True:
            try:
                self.process_turn()
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
            print(self._rules["instructions"])
        elif result.lower() == "exit":
            raise ExitException()
        elif result.isdigit() and int(result) in self._rules["game_map"]:
            self._resolve_turn(int(result))
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
                        for key, value in self._rules["game_map"].items()
                    ]
                )
            )
        )

        print()

        # Player Input
        result = input("Enter your move : ")
        logger.debug("get value: %s", result)

        return result

    def _resolve_turn(self, player_move):
        # Get the computer move
        comp_move = self._get_ai_move()
        print(f"Computer chooses {self._rules['game_map'][comp_move]}")

        # Find the winner of the match
        winner = self._get_winner(player_move, comp_move)

        # Declare the winner
        if winner == player_move:
            result = f"{self._user.name} WINS!!!"
            self._user.add_win()
        elif winner == comp_move:
            result = "COMPUTER WINS!!!"
            self._user.add_loss()
        else:
            result = "TIE GAME"

        print(result)
        print(f"Your new score: {self._user.score}")

    def _get_ai_move(self):
        print("Computer making a move ...")
        time.sleep(0.2)
        possible_move = list(self._rules["game_map"].keys())
        return random.choice(possible_move)

    def _get_winner(self, move_1, move_2):
        return self._rules["winner"][move_1][move_2]
