import requests

def http_get(url):

    r = requests.get(url)

    return r.text


def http_post(url, data):

    r = requests.post(url, json=data)

    return r.text
