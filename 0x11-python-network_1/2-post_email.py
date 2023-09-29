#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    custom_url = argv[1]
    custom_value = {"email": argv[2]}
    custom_data = urlencode(custom_value).encode("ascii")
    custom_request = Request(custom_url, custom_data)

    with urlopen(custom_request) as custom_response:
        print(custom_response.read().decode("utf-8", "replace"))
