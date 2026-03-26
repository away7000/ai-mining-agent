from tools.http_tool import http_get, http_post


def execute_call(url, method="GET", data=None):

    if method == "GET":
        return http_get(url)

    if method == "POST":
        return http_post(url, data)
