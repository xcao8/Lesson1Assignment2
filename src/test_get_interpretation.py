from unittest.mock import patch
from get_interpretation import get_interpretation


@patch("get_interpretation.client.post_message", return_value={"title": "ECU Reset"})
def test_get_interpretation_with_id_11(mock_post_message):
    assert get_interpretation("11") == mock_post_message()


@patch("get_interpretation.client.post_message", return_value={"title": "Security Access"})
def test_get_interpretation_with_id_27(mock_post_message):
    assert get_interpretation("11") == mock_post_message()
