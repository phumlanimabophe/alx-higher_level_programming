#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
from sys import argv
import requests

if __name__ == "__main__":
    custom_letter = "" if len(argv) == 1 else argv[1]
    custom_request = requests.post("http://0.0.0.0:5000/search_user", {"q": custom_letter})

    try:
        custom_response = custom_request.json()
        if custom_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(custom_response.get("id"), custom_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
