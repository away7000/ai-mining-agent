import time
import requests
from skill_parser import parse_skill
from tools.wallet import address

def run_mining():

    print("WALLET:", address())

    urls = parse_skill()

    for url in urls:

        try:

            r = requests.get(url, timeout=10)

            print(r.text)

        except Exception as e:

            print(e)

def auto_mining_loop():

    while True:

        run_mining()

        time.sleep(20)
