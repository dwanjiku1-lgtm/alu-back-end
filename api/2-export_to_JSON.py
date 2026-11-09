#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": user_id}
    ).json()

    username = user.get("username")

    data = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            for task in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(data, json_file)
