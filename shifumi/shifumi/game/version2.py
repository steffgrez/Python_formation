rules = {
    "instructions": """
    Instructions for Rock-Paper-Scissors-Lizard-Spock : 

    Scissors cuts Paper
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    Rock crushes Scissors
    """,
    "game_map": {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "Spock"},
    "winner": [
        [-1, 1, 0, 0, 4],
        [1, -1, 2, 3, 1],
        [0, 2, -1, 2, 4],
        [0, 3, 2, -1, 3],
        [4, 1, 4, 3, -1],
    ],
}
