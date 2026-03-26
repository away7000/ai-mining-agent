import requests
from config import SKILL_URL

def load_skill():

    try:
        r = requests.get(SKILL_URL, timeout=10)
        return r.text
    except:
        return ""
