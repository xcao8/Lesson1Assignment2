import json
from requests import post


def post_message(url, payload): # pylint: disable=missing-function-docstring
    headers = {"content-type": "application/json"}
    response = post(url, data=json.dumps(payload), headers=headers)
    return response.json()
