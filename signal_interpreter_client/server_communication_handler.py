import json
import logging
from requests import post, exceptions

logger = logging.getLogger(__name__)


class SignalInterpreterClientConnectionError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class SignalInterpreterClientConnectionUnsuccessfulError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def post_message(url, payload):
    headers = {"content-type": "application/json"}
    try:
        response = post(url, data=json.dumps(payload), headers=headers)
        logger.info("Post request to server...")
        response.raise_for_status()
        return response.json()
    except exceptions.ConnectionError as ConErr:
        logger.exception("Exception occurred: %s", ConErr)
        raise SignalInterpreterClientConnectionError() from ConErr
    except exceptions.HTTPError as ErrHttp:
        logger.exception("Exception occurred: %s", ErrHttp)
        raise SignalInterpreterClientConnectionUnsuccessfulError() from ErrHttp
