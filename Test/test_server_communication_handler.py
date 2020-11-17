import server_communication_handler
import json
from unittest.mock import patch


@patch("server_communication_handler.post")
def test_post_message(mock_post):
    server_communication_handler.post_message("http://127.0.0.1:5000/",{"signal": "11"})
    mock_post.assert_called_once()
    mock_post.assert_called_with("http://127.0.0.1:5000/",data=json.dumps({"signal": "11"}),headers={"content-type": "application/json"})

'''
@patch("requests.post",return_value="Security Access")
def test_server_communication_handler_with_ID_27(mock_post):
    assert post_message("http://127.0.0.1:5000/",{"id": "27"})=={"title": "Security Access"}
'''



