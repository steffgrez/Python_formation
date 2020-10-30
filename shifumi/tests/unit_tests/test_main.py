from unittest.mock import MagicMock, patch

import pytest

from shifumi import main


@patch("shifumi.main.storage")
@patch("shifumi.main.User")
@patch("builtins.input", side_effect=["toto", "1", "3"])
def test_main_version1(input_mock, user_mock, db_mock):
    with patch("shifumi.main.Game") as game_mock:
        main.main()
        user_mock.assert_called_with("toto", db_mock.DB())
        game_mock.assert_called_with(user_mock(), "1")
        assert input_mock.call_count == 3
