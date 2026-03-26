from openai import OpenAI
from config import OPENROUTER_KEY, MODEL
from skill_loader import load_skill

client = OpenAI(
    api_key=OPENROUTER_KEY,
    base_url="https://openrouter.ai/api/v1"
)

skill_text = load_skill()


SYSTEM_PROMPT = f"""
You are AI Agent.

Use this skill:

{skill_text}

Always follow the skill instructions.
"""


def ask_ai(text):

    res = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ]
    )

    return res.choices[0].message.content
