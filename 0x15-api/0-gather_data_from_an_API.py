#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""


if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) < 2 or not argv[1].isdigit():
        exit()

    user_id = argv[1]
    user_name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
        ).json().get("name")

    tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        ).json()

    completed_tasks = []
    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, len(completed_tasks), len(tasks)))

    for title in completed_tasks:
        print(f"\t {title}")
