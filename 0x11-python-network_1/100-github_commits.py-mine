#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the repository rails'
by the user 'rails'"""
import requests
from sys import argv


if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)

    r = requests.get(url)
    try:
        r = r.json()
        count = 0
        for commit in r:
            if count < 10:
                sha = commit.get('sha')
                author = commit.get('commit').get('author').get('name')
                print('{}: {}'.format(sha, author))
            count += 1
    except ValueError:
        print('Not a valid JSON')
