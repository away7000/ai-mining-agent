
from web3 import Web3
from config import PRIVATE_KEY, RPC

w3 = Web3(Web3.HTTPProvider(RPC))

account = w3.eth.account.from_key(PRIVATE_KEY)


def address():

    return account.address
    
def balance():

    bal = w3.eth.get_balance(account.address)

    return w3.from_wei(bal, "ether")
