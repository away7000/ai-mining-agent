import os
from web3 import Web3

PRIVATE_KEY = os.environ["PRIVATE_KEY"]
RPC = os.environ["RPC"]

w3 = Web3(Web3.HTTPProvider(RPC))

account = w3.eth.account.from_key(PRIVATE_KEY)


def address():
    return account.address


def balance():
    bal = w3.eth.get_balance(account.address)
    return w3.from_wei(bal, "ether")


def get_account():
    return account
