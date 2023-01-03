#!/usr/bin/python3
"""Takes URL sends request and displays value of X-Request-Id"""
import urllib.request
from sys import argv

if len(argv) > 1:
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
