from unittest.mock import patch, call


@patch("builtins.print")
def test_main(mock_print):
    mock_print.mock_calls = [call("ECU Reset")]
