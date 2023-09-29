#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    custom_url = argv[1]
    custom_request = Request(custom_url)

    with urlopen(custom_request) as custom_response:
        print(dict(custom_response.headers).get("X-Request-Id"))
