#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
