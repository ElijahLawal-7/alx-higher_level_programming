#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses the GitHub
API to display your id"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    try:
        print(r.json().get('id'))
    except ValueError:
        print('Not a valid JSON')
