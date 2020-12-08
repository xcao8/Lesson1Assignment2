import responses
from unittest.mock import patch, call
from unittest.mock import patch
import sys
from signal_interpreter_client.main import main


@patch.object(sys, "argv", ["signal_interpreter_client", "--signal", "11"])
@responses.activate
@patch("builtins.print")
def test_server_integration(mock_print):
    responses.add(
        responses.POST,
        "http://127.0.0.1:5000/",
        json="ECU Reset",
    )
    main()
    assert mock_print.mock_calls == [call("ECU Reset")]

