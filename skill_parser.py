import re
from skill_loader import load_skill


def parse_skill():

    text = load_skill()

    print(text[:200])

    urls = re.findall(
        r"https?://[^\s)]+",
        text
    )

    return urls
