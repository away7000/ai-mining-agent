from openai import OpenAI
from config import OPENROUTER_KEY, MODEL
from skill_loader import load_skill
from router import run_tool
import json


client = OpenAI(
    api_key=OPENROUTER_KEY,
    base_url="https://openrouter.ai/api/v1"
)


skill = load_skill()


SYSTEM = f"""
You are AI Mining Agent

You can use tools.

Skill:

{skill}

When you need tool:

return JSON

{{
 "tool": "http_get",
 "args": {{}}
}}
"""


def ask_ai(text):

    res = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": text}
        ]
    )

    msg = res.choices[0].message.content

    try:

        data = json.loads(msg)

        if "tool" in data:

            result = run_tool(
                data["tool"],
                data.get("args", {})
            )

            return str(result)

    except:
        pass

    return msg
