from tools.http_tool import http_get, http_post
from tools.wallet import address
from tools.mining_tool import execute_call


TOOLS = {
    "http_get": http_get,
    "http_post": http_post,
    "wallet_address": address,
    "execute": execute_call,
}


def run_tool(name, args):

    if name in TOOLS:
        return TOOLS[name](**args)

    return "tool not found"
