import re
from skill_loader import load_skill


def parse_skill():

    text = load_skill()

    urls = re.findall(
        r"https?://[^\s)]+",
        text
    )

    return urls
