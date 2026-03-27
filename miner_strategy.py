import time
import requests

from miner_contract import mine, claim_eth

API = "https://api.mineloot.app/api/round/current"

LAST_ROUND = None
DEPLOYED = False


def get_round():

    return requests.get(API).json()


def pick_best_block(data):

    blocks = data["blocks"]

    best = None
    best_val = None

    for b in blocks:

        val = int(b["deployed"])

        if best_val is None or val < best_val:
            best_val = val
            best = b["id"]

    return best


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
            if 8 > remain > 2 and not DEPLOYED:

                block = pick_best_block(data)

                print("DEPLOY", block)

                try:

                    tx = mine([block])

                    print(tx)

                    DEPLOYED = True

                except Exception as e:

                    print("DEPLOY ERR", e)

                time.sleep(5)

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
