#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body
of the response.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    custom_url = argv[1]
    custom_value = {"email": argv[2]}
    custom_request = requests.post(custom_url, data=custom_value)

    print(custom_request.text)
