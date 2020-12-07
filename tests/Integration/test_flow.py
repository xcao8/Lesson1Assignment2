import responses
from unittest.mock import patch
import sys
from signal_interpreter_client.main import main


@patch.object(sys, "argv", ["signal_interpreter_client", "--signal", "11"])
@responses.activate
def test_server_integration():
    responses.add(
        responses.POST,
        "http://127.0.0.1:5000/",
        json="ECU Reset",
       #status=200
    )
    print("here")
    assert main() == "ECU Reset"