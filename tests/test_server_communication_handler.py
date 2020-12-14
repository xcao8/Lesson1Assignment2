from unittest.mock import patch
import json
import pytest
from requests.exceptions import Timeout, HTTPError
from requests.exceptions import ConnectionError as MyConnectionError
from signal_interpreter_client.server_communication_handler import SignalInterpreterClientConnectionError, \
    SignalInterpreterClientConnectionUnsuccessfulError, post_message


@patch("signal_interpreter_client.server_communication_handler.post")
def test_post_message(mock_post):
    post_message("http://127.0.0.1:5000/", {"signal": "11"})
    mock_post.assert_called_once()
    mock_post.assert_called_with("http://127.0.0.1:5000/", data=json.dumps({"signal": "11"}),
                                 headers={"content-type": "application/json"})


@patch("signal_interpreter_client.server_communication_handler.post", side_effect=Timeout)
def test_post_message_with_timeout(mock_post):
    with pytest.raises(Timeout):
        post_message("http://127.0.0.1:5000/", {"signal": "11"})
        mock_post.assert_called_once()
        mock_post.assert_called_with("http://127.0.0.1:5000/", data=json.dumps({"signal": "11"}),
                                     headers={"content-type": "application/json"})


@patch("signal_interpreter_client.server_communication_handler.post", side_effect=MyConnectionError)
def test_post_message_with_conn_err(mock_post):
    with pytest.raises(SignalInterpreterClientConnectionError):
        post_message("http://127.0.0.1:5000/", {"signal": "11"})
        mock_post.assert_called_once()
        mock_post.assert_called_with("http://127.0.0.1:5000/", data=json.dumps({"signal": "11"}),
                                     headers={"content-type": "application/json"})


@patch("signal_interpreter_client.server_communication_handler.post", side_effect=HTTPError)
def test_post_message_with_http_err(mock_post):
    with pytest.raises(SignalInterpreterClientConnectionUnsuccessfulError):
        post_message("http://127.0.0.1:5000/", {"signal": "11"})
        mock_post.assert_called_once()
        mock_post.assert_called_with("http://127.0.0.1:5000/", data=json.dumps({"signal": "11"}),
                                     headers={"content-type": "application/json"})
