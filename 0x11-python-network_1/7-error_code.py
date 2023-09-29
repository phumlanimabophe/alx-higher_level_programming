#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response.

Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
from sys import argv
import requests

if __name__ == "__main__":
    custom_url = argv[1]
    custom_request = requests.get(custom_url)

    if custom_request.status_code >= 400:
        print("Error code: {}".format(custom_request.status_code))
    else:
        print(custom_request.text)
