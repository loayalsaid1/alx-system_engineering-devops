#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""


import requests
import json
import sys
try:
    user_id = sys.argv[1]
except Exception:
    exit()

user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
user = json.loads(user.text)

tasks = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")
tasks = json.loads(tasks.text)

tasks_number = 0
completed_tasks = 0
titles = []

for task in tasks:
    tasks_number += 1
    if task['completed']:
        completed_tasks += 1
        titles.append(task['title'])

print(f"Employee {user['name']}",
      f"is done with tasks({completed_tasks}/{tasks_number}):")
for title in titles:
    print(f"\t{title}")
