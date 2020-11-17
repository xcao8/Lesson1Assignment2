from get_interpretation import get_interpretation
import pytest
from unittest.mock import patch

@patch("client.post_message",return_value={"title": "ECU Reset"})
def test_get_interpretation_with_ID_11(mock_post_message):
    assert get_interpretation("11")==mock_post_message()


@patch("client.post_message", return_value={"title": "Security Access"})
def test_get_interpretation_with_ID_27(mock_post_message):
    assert get_interpretation("11") == mock_post_message()


