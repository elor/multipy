from multipy_common import deserialize
import requests


def retrieve(host='127.0.0.1', port='8000'):
    url = 'http://{}:{}/'.format(host, port)
    response = requests.get(url)
    return deserialize(response.content.decode('utf-8'))
