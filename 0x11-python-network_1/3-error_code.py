#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    custom_url = argv[1]
    custom_request = Request(custom_url)

    try:
        with urlopen(custom_request) as custom_response:
            print(custom_response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
