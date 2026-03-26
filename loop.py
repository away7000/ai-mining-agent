import time
from agent import ask_ai

RUN = True


def auto_loop():

    while RUN:

        try:

            print("AI thinking...")

            res = ask_ai(
                "check mining status and run mining or claim if needed"
            )

            print(res)

        except Exception as e:
            print(e)

        time.sleep(20)
