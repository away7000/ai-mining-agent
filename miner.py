import time
import requests
from skill_parser import parse_skill
from tools.wallet import address
from tools.wallet import address, get_account
from eth_account.messages import encode_defunct

def run_mining():

    urls = parse_skill()

    addr = address()

    msg, sig = sign_message()

    for url in urls:

        try:

            r = requests.post(
                url,
                json={
                    "wallet": addr,
                    "message": msg,
                    "signature": sig
                },
                timeout=10
            )

            print(r.text)

        except Exception as e:

            print(e)
            
def auto_mining_loop():

    while True:

        run_mining()

        time.sleep(20)
        
def sign_message():

    acc = get_account()

    msg = str(int(time.time()))

    message = encode_defunct(text=msg)

    signed = acc.sign_message(message)

    return msg, signed.signature.hex()
