#!/usr/bin/python3
"""Use an api"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
        ).json().get('name')

    tasks = requests.get(
                f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    ).json()

    with open("USER_ID.csv", "w") as f:
        writer = csv.writer(f)
        for task in tasks:
            row = [
                f"{user_id}",
                f"{user_name}",
                f"{task.get('completed')}",
                f"{task.get('title')}"
            ]
            writer.writerow(row)
