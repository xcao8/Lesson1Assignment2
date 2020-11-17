import server_communication_handler as client


def get_interpretation(signal):
    url = "http://127.0.0.1:5000/"
    payload={"signal": signal}
    return client.post_message(url, payload)

