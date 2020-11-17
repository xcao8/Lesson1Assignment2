from server_communication_handler import post_message
import json
import pytest
from unittest.mock import patch


@patch("requests.post")
def test_server_communication_handler_with_ID_11(mock_post):
    # assert post_message("http://127.0.0.1:5000/",{"id": "11"})=={"title": "ECU Reset"}
    post_message("http://127.0.0.1:5000/",{"id": "11"})
    mock_post.assert_called_with("http://127.0.0.1:5000/",data=json.dumps({"id": "11"}),headers={"content-type": "application/json"})

'''
@patch("requests.post",return_value="Security Access")
def test_server_communication_handler_with_ID_27(mock_post):
    assert post_message("http://127.0.0.1:5000/",{"id": "27"})=={"title": "Security Access"}
'''



