import time
import requests
from skill_parser import parse_skill


def run_mining():

    urls = parse_skill()

    print("URLS:", urls)

    for url in urls:

        try:

            print("CALL", url)

            r = requests.get(url, timeout=10)

            print("RESP:", r.status_code)

        except Exception as e:

            print("ERR", e)



def auto_mining_loop():

    while True:

        run_mining()

        time.sleep(20)
