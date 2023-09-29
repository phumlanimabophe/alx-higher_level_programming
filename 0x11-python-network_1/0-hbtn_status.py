#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status."""
from urllib.request import Request, urlopen

if __name__ == "__main__":
    custom_request = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(custom_request) as custom_response:
        response_body = custom_response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode("utf-8")))
