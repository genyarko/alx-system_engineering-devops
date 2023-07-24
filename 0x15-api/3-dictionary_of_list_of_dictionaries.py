#!/usr/bin/python3

"""
Module: gather_data_from_an_API

Script to fetch TODO list progress for all employees using REST API and export data to JSON format.

Usage:
    python3 gather_data_from_an_API.py
"""

import requests
import json

def get_all_employees_todo_list_progress():
    """
    Fetch the TODO list progress for all employees and export to JSON format.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    response_users = requests.get(users_url)
    response_todos = requests.get(todos_url)

    users_data = response_users.json()
    todos_data = response_todos.json()

    all_employees_data = {}

    for user in users_data:
        employee_id = user['id']
        employee_name = user['name']

        tasks = [
            {
                "username": employee_name,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in todos_data if task['userId'] == employee_id
        ]

        all_employees_data[employee_id] = tasks

    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as file:
        json.dump(all_employees_data, file, indent=4)

    print(f"Data for all employees exported to {json_file}")

if __name__ == "__main__":
    get_all_employees_todo_list_progress()
