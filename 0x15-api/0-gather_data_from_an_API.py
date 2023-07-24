#!/usr/bin/python3
"""
Module: gather_data_from_an_API
Script to fetch TODO list progress for a given employee ID using REST API.
Usage:
    python3 gather_data_from_an_API.py <employee_id>
"""

import requests
import sys

def get_employee_data(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    todos_response = requests.get(url + "todos", params={"userId": employee_id})

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    completed = [todo.get("title") for todo in todos if todo.get("completed")]
    return user, completed, len(todos)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user, completed, total_tasks = get_employee_data(employee_id)

    print(f"Employee {user.get('name')} is done with tasks({len(completed)}/{total_tasks}):")
    [print(f"\t {c}") for c in completed]

