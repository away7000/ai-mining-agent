import re
from skill_loader import load_skill
from tools.wallet import address

WALLET = address()

def parse_skill():

    text = load_skill()

    print(text[:200])

    urls = re.findall(
        r"https?://[^\s)]+",
        text
    )

    return urls
