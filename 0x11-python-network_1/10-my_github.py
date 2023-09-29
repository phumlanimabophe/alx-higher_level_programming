#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    custom_auth = HTTPBasicAuth(argv[1], argv[2])
    custom_request = requests.get("https://api.github.com/user", auth=custom_auth)

    print(custom_request.json().get("id"))
