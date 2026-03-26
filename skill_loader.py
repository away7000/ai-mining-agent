import requests
from config import SKILL_URL

def load_skill():

    r = requests.get(SKILL_URL)

    if r.status_code != 200:
        return ""

    return r.text
