#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    custom_request = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(custom_request.text)))
    print("\t- content: {}".format(custom_request.text))
