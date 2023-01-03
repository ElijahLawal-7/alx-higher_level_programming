#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t-".format(
              type(html), html), "utf8 content:", html.decode("utf-8"))
