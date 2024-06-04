#!/usr/bin/python3
"""Use an api"""
import json
import requests


if __name__ == "__main__":

    users = requests.get(
        f"https://jsonplaceholder.typicode.com/users"
        ).json()

    final_answer = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        user_tasks = []

        tasks = requests.get(
                f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        ).json()

        for task in tasks:
            needed_info = {}
            needed_info['username'] = username
            needed_info['task'] = task['title']
            needed_info['completed'] = task['completed']

            user_tasks.append(needed_info)

        final_answer[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(final_answer, f)
