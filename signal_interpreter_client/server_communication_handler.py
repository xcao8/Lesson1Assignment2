import json
import logging
from requests import post, exceptions

logger = logging.getLogger(__name__)


class SignalInterpreterClientConnectionError(Exception):
    """Empty class"""


class SignalInterpreterClientConnectionUnsuccessfulError(Exception):
    """Empty class"""


def post_message(url, payload):
    headers = {"content-type": "application/json"}
    try:
        response = post(url, data=json.dumps(payload), headers=headers)
        logger.info("Post request to server...")
        response.raise_for_status()
        return response.json()
    except exceptions.ConnectionError as con_err:
        logger.exception("Exception occurred: %s", con_err)
        raise SignalInterpreterClientConnectionError() from con_err
    except exceptions.HTTPError as err_http:
        logger.exception("Exception occurred: %s", err_http)
        raise SignalInterpreterClientConnectionUnsuccessfulError() from err_http
