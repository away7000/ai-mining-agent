import time
import requests
import random

from miner_contract import mine, claim_eth

API = "https://api.mineloot.app/api/round/current"

LAST_ROUND = None
DEPLOYED = False


def get_round():

    r = requests.get(API)

    return r.json()


def random_count():

    return random.choice([1, 2, 3])


def pick_random_blocks(n):

    blocks = list(range(25))

    random.shuffle(blocks)

    return blocks[:n]


def auto_strategy():

    global LAST_ROUND, DEPLOYED

    while True:

        try:

            data = get_round()

            rid = data["roundId"]
            end = data["endTime"]

            now = int(time.time())

            remain = end - now

            print("ROUND", rid, "remain", remain)

            # new round
            if rid != LAST_ROUND:

                LAST_ROUND = rid
                DEPLOYED = False

                print("NEW ROUND")


            # deploy
            if remain <= 15 and remain >= 5 and not DEPLOYED:

                n = random_count()

                blocks = pick_random_blocks(n)

                print("DEPLOY", blocks)

                try:

                    tx = mine(blocks)

                    print("TX", tx)

                    DEPLOYED = True

                except Exception as e:

                    print("DEPLOY ERR", e)


            # claim
            if remain < 1 and DEPLOYED:

                try:

                    tx = claim_eth()

                    print("CLAIM", tx)

                except Exception as e:

                    print("CLAIM ERR", e)


        except Exception as e:

            print("LOOP ERR", e)


        time.sleep(2)
