import time
import requests
import random

from miner_contract import mine, claim_eth

API = "https://api.mineloot.app/api/round/current"

LAST_ROUND = None
DEPLOYED = False


def get_round():

    return requests.get(API).json()


def pick_blocks(data, n=3):

    blocks = data["blocks"]

    arr = []

    for b in blocks:

        arr.append(
            (int(b["deployed"]), b["id"])
        )

    arr.sort()

    result = []

    for i in range(n):
        result.append(arr[i][1])

    return result
    
def pick_random_blocks(n=3):

    blocks = list(range(25))

    random.shuffle(blocks)

    return blocks[:n]

def random_count():

    return random.choice([1, 2, 3, 4, 5])

def should_play(data):

    total = int(data["totalDeployed"])

    # skip if pool too small
    if total < 1000000000000000:
        return False

    return True


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

            # decide play
            if not should_play(data):

                time.sleep(2)
                continue

            # deploy near end
            if remain <= 15 and remain >= 5 and not DEPLOYED:

            blocks = pick_random_blocks(random_count())

            print("DEPLOY", blocks)

                try:

                    tx = mine(blocks)

                    print("TX", tx)

             DEPLOYED = True

                except Exception as e:

                    print("DEPLOY ERR", e)

            # claim after end
            if remain < 1:

                try:

                    tx = claim_eth()

                    print("CLAIM", tx)

                except Exception as e:

                    print("CLAIM ERR", e)

                time.sleep(5)

        except Exception as e:

            print("LOOP ERR", e)

        time.sleep(2)
