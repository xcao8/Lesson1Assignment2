from unittest.mock import patch
from src.get_interpretation import get_interpretation


@patch("src.get_interpretation.client.post_message", return_value={"title": "ECU Reset"})
def test_get_interpretation_with_ID_11(mock_post_message):
    assert get_interpretation("11") == mock_post_message()


@patch("src.get_interpretation.client.post_message", return_value={"title": "Security Access"})
def test_get_interpretation_with_ID_27(mock_post_message):
    assert get_interpretation("11") == mock_post_message()
