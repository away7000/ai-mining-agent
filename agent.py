from openai import OpenAI
from config import OPENROUTER_KEY, MODEL
from skill_loader import load_skill
from router import run_tool
import json


client = OpenAI(
    api_key=OPENROUTER_KEY,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://localhost",
        "X-Title": "mining-agent"
    }
)


skill = load_skill()


SYSTEM = f"""
You are AUTO MINING AI AGENT

Your job:

- always run mining
- always check claim
- always follow skill
- never stop mining

Skill:

{skill}

If you need tool return JSON like this:

{{
 "tool": "http_get",
 "args": {{}}
}}
"""


def ask_ai(text):

    try:

        res = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": text}
            ],
            timeout=20,
        )

        msg = res.choices[0].message.content

    except Exception as e:
        return f"AI ERROR: {e}"

    return msg
