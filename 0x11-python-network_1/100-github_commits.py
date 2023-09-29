#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    try:
        response = requests.get(url)
        commits = response.json()
        
        if response.status_code == 200:
            for commit in commits[:10]:  # Get the most recent 10 commits
                sha = commit.get("sha")
                author_name = commit.get("commit").get("author").get("name")
                print(f"{sha}: {author_name}")
        else:
            print("Error: Unable to fetch commits")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
