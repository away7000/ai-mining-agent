import os
from web3 import Web3
from tools.wallet import get_account

RPC = os.environ["RPC"]

w3 = Web3(Web3.HTTPProvider(RPC))

account = get_account()

ADDRESS = account.address


CONTRACT_ADDR = Web3.to_checksum_address(
    "0xA8E2F506aDcbBF18733A9F0f32e3D70b1A34d723"
)


ABI = [
    {
        "name": "deploy",
        "type": "function",
        "stateMutability": "payable",
        "inputs": [
            {"name": "blockIds", "type": "uint8[]"}
        ],
        "outputs": []
    },
    {
        "name": "claimETH",
        "type": "function",
        "inputs": [],
        "outputs": []
    },
    {
        "name": "claimLOOT",
        "type": "function",
        "inputs": [],
        "outputs": []
    }
]


contract = w3.eth.contract(
    address=CONTRACT_ADDR,
    abi=ABI
)


def send_tx(tx):

    signed = account.sign_transaction(tx)

    raw = getattr(
        signed,
        "rawTransaction",
        getattr(signed, "raw_transaction")
    )

    tx_hash = w3.eth.send_raw_transaction(raw)

    return tx_hash.hex()
    
def mine(blocks):

    nonce = w3.eth.get_transaction_count(ADDRESS)

    tx = contract.functions.deploy(blocks).build_transaction({
        "from": ADDRESS,
        "value": w3.to_wei(0.0000025, "ether"),
        "nonce": nonce,
        "gas": 300000,
        "gasPrice": w3.eth.gas_price,
        "chainId": 8453,
    })

    return send_tx(tx)

def claim_eth():

    nonce = w3.eth.get_transaction_count(ADDRESS)

    tx = contract.functions.claimETH().build_transaction({
        "from": ADDRESS,
        "nonce": nonce,
        "gas": 200000,
        "gasPrice": w3.eth.gas_price,
        "chainId": 8453,
    })

    return send_tx(tx)


def claim_loot():

    nonce = w3.eth.get_transaction_count(ADDRESS)

    tx = contract.functions.claimLOOT().build_transaction({
        "from": ADDRESS,
        "nonce": nonce,
        "gas": 200000,
        "gasPrice": w3.eth.gas_price,
        "chainId": 8453,
    })

    return send_tx(tx)
