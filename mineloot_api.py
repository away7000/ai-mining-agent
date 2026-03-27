import requests
from tools.wallet import address

API = "https://api.mineloot.app/api"


def get_rewards():

    addr = address()

    url = f"{API}/user/{addr}/rewards"

    r = requests.get(url).json()

    return r


def get_user():

    addr = address()

    url = f"{API}/user/{addr}"

    r = requests.get(url).json()

    return r
