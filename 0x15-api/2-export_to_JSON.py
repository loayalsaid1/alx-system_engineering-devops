#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""


import requests
import json
import sys
try:
    user_id = sys.argv[1]
except Exception:
    exit()

tasks = requests.get(
    f"https://jsonplaceholder.typicode.com/todos/{user_id}")
tasks = json.loads(tasks.text)
print(tasks)
