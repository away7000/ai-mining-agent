import requests
from tools.wallet import address

API = "https://api.mineloot.app/api"


def get_rewards():

    addr = address()

    url = f"{API}/user/{addr}/rewards"

    return requests.get(url).json()


def get_user():

    addr = address()

    url = f"{API}/user/{addr}"

    return requests.get(url).json()
