#!/usr/bin/python3
"""
 save items to a file.
"""

import sys
import os.path

args = sys.argv[1:]

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

item = []
if os.path.exists("./add_item.json"):
    item = load_from_json_file("add_item.json")

save_to_json_file(item + args, "add_item.json")
