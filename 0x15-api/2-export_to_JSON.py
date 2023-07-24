#!/usr/bin/python3
"""
Module: gather_data_from_an_API

Script to fetch TODO list progress for a given employee ID using REST API and export data to JSON format.

Usage:
    python3 gather_data_from_an_API.py <employee_id>
"""

import sys
import requests
import json

def get_employee_todo_list_progress(employee_id):
    """
    Fetch and display the TODO list progress for the given employee ID and export to JSON format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    response_user = requests.get(user_url)
    response_todos = requests.get(todos_url)

    user_data = response_user.json()
    todos_data = response_todos.json()

    employee_name = user_data['name']

    json_data = {
        "USER_ID": [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            }
            for task in todos_data
        ]
    }

    json_file = f'{employee_id}.json'
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f"Employee {employee_name} data exported to {json_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
