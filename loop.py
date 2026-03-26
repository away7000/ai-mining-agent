import time
from agent import ask_ai

RUN = True


def auto_loop():

    while True:

        ask_ai("mine")

        time.sleep(10)

        ask_ai("claim")

        time.sleep(30)
