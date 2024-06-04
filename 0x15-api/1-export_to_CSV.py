#!/usr/bin/python3
"""Use an api"""
import csv
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

    with open(f"{user_id}.csv", "w", newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            row = [
                user_id,
                user_name,
                task.get('completed'),
                task.get('title')
            ]
            writer.writerow(row)
