#!/usr/bin/python3
"""Use an api"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
        ).json().get('username')

    tasks = requests.get(
                f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    ).json()

    result = []
    for task in tasks:
        r = {}
        r['task'] = task['title']
        r['completed'] = task['completed']
        r['username'] = user_name
        result.append(r)

    final_result = {f"{user_id}": result}
    with open(f"{user_id}.json", "w") as f:
        json.dump(final_result, f)
