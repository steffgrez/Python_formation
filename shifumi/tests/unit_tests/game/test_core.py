from unittest.mock import MagicMock, patch

import pytest

from shifumi.game.core import Game, InputException, ExitException

@pytest.fixture
def user_mock():
    return MagicMock()

def my_random_choice_1(a):
    return 1


def test_init(user_mock):
    with pytest.raises(InputException):
        game = Game(user_mock, "3")

@patch("builtins.input")
def test_process_turn(mock_input, user_mock):
    game = Game(user_mock, "1") 

    mock_input.return_value = 'toto'
    with pytest.raises(InputException):
        game.process_turn()

    mock_input.return_value = 'exit'
    with pytest.raises(ExitException):
        game.process_turn()

    with patch.object(Game, '_resolve_turn') as mock_method:
        mock_input.return_value = '1'
        game.process_turn()
        mock_method.assert_called_with(1)

@patch.object(Game, '_get_ai_move')
def test_resolve_turn(mock_get_ai_move, user_mock):
    game = Game(user_mock, "1") 

    mock_get_ai_move.return_value = 2
    game._resolve_turn(1)
    user_mock.add_wins.assert_not_called()
    user_mock.add_loss.assert_called()

    user_mock.reset_mock()
    mock_get_ai_move.return_value = 2
    game._resolve_turn(0)
    user_mock.add_loss.assert_not_called()
    user_mock.add_win.assert_called()

    user_mock.reset_mock()
    mock_get_ai_move.return_value = 2
    game._resolve_turn(2)
    user_mock.add_loss.assert_not_called()
    user_mock.add_win.assert_not_called()


def test_get_ai_move(user_mock):
    game = Game(user_mock, "1")

    with patch("random.choice", my_random_choice_1):
        assert game._get_ai_move() == 1

@pytest.mark.parametrize(
    "move1,move2,winner", [(1, 1, -1), (1, 2, 2)]
)
def test_get_winner(move1, move2, winner, user_mock):
    game = Game(user_mock, "1")

    assert game._get_winner(move1, move2) == winner