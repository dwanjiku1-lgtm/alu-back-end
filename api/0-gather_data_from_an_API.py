#!/usr/bin/python3
"""Show how far an employee has got with their TODO list.

Give this script an employee ID and it asks the JSONPlaceholder API
for that person's name and tasks. It then prints how many tasks they
have finished out of the total, followed by the title of each
finished task.

Usage:
    python3 0-gather_data_from_an_API.py 2
"""
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    employee_id = int(sys.argv[1])
    user = requests.get("{}/users/{}".format(API_URL, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(API_URL), params={"userId": employee_id}
    ).json()
    completed = [t.get("title") for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for title in completed:
        print("\t {}".format(title))