import os
import time
import requests

from miner_contract import mine, claim_eth

API = "https://api.mineloot.app/api/round/current"


LAST_ROUND = None


def get_round():

    r = requests.get(API).json()

    return r


def auto_loop():

    global LAST_ROUND

    while True:

        try:

            data = get_round()

            round_id = data["roundId"]
            end = data["endTime"]

            now = int(time.time())

            remain = end - now

            print("ROUND", round_id, "remain", remain)

            # new round
            if LAST_ROUND != round_id:

                LAST_ROUND = round_id

                print("new round")

            # deploy near end
            if remain < 10 and remain > 2:

                print("DEPLOY")

                try:
                    tx = mine()
                    print(tx)
                except Exception as e:
                    print(e)

                time.sleep(5)

            # claim after round
            if remain < 1:

                print("CLAIM")

                try:
                    tx = claim_eth()
                    print(tx)
                except Exception as e:
                    print(e)

                time.sleep(5)

        except Exception as e:

            print("ERR", e)

        time.sleep(2)
